###############################################################################
#   actionAngle: a Python module to calculate  actions, angles, and frequencies
#
#      class: actionAngleIsochroneApprox
#
#             Calculate actions-angle coordinates for any potential by using 
#             an isochrone potential as an approximate potential and using 
#             a Fox & Binney (2013?) + torus machinery-like algorithm 
#             (angle-fit)
#
#      methods:
#             __call__: returns (jr,lz,jz)
#
###############################################################################
import copy
import math
import numpy as nu
import numpy.linalg as linalg
from scipy import optimize
from galpy.potential import dvcircdR, vcirc
from galpy.orbit import Orbit
from galpy.actionAngle import actionAngleIsochrone
from actionAngle import actionAngle
from galpy.potential import IsochronePotential
_TWOPI= 2.*nu.pi
class actionAngleIsochroneApprox():
    """Action-angle formalism using an isochrone potential as an approximate potential and using a Fox & Binney (2013?) like algorithm to calculate the actions using orbit integrations and a torus-machinery-like angle-fit to get the angles and frequencies"""
    def __init__(self,*args,**kwargs):
        """
        NAME:
           __init__
        PURPOSE:
           initialize an actionAngleIsochroneApprox object
        INPUT:
           Either:
              b= scale parameter of the isochrone parameter
              ip= instance of a IsochronePotential
              aAI= instance of an actionAngleIsochrone
           pot= potential to calculate action-angle variables for
           tintJ= (default: 100) time to integrate orbits for to estimate 
                  actions
           ntintJ= (default: 10000) number of time-integration points
                  actions
           integrate_method= (default: 'dopr54_c') integration method to use
        OUTPUT:
        HISTORY:
           2013-09-10 - Written - Bovy (IAS)
        """
        if not kwargs.has_key('pot'):
            raise IOError("Must specify pot= for actionAngleStaeckel")
        self._pot= kwargs['pot']
        if not kwargs.has_key('b') and not kwargs.has_key('ip') \
                and not kwargs.has_key('aAI'):
            raise IOError("Must specify b=, ip=, or aAI= for actionAngleIsochroneApprox")
        if kwargs.has_key('aAI'):
            if not isinstance(kwargs['aAI'],actionAngleIsochrone):
                raise IOError("'Provided aAI= does not appear to be an instance of an actionAngleIsochrone")
            self._aAI= kwargs['aAI']
        elif kwargs.has_key('ip'):
            ip= kwargs['ip']
            if not isinstance(ip,IsochronePotential):
                raise IOError("'Provided ip= does not appear to be an instance of an IsochronePotential")
            self._aAI= actionAngleIsochrone(ip=ip)
        else:
            self._aAI= actionAngleIsochrone(ip=IsochronePotential(b=kwargs['b'],
                                                                  normalize=1.))
        if kwargs.has_key('tintJ'):
            self._tintJ= kwargs['tintJ']
        else:
            self._tintJ= 100.
        if kwargs.has_key('ntintJ'):
            self._ntintJ= kwargs['ntintJ']
        else:
            self._ntintJ= 10000
        self._tsJ= nu.linspace(0.,self._tintJ,self._ntintJ)
        if kwargs.has_key('integrate_method'):
            self._integrate_method= kwargs['integrate_method']
        else:
            self._integrate_method= 'dopr54_c'
        self._c= False
        ext_loaded= False
        if ext_loaded and ((kwargs.has_key('c') and kwargs['c'])
                           or not kwargs.has_key('c')):
            self._c= True
        else:
            self._c= False
        return None
    
    def __call__(self,*args,**kwargs):
        """
        NAME:
           __call__
        PURPOSE:
           evaluate the actions (jr,lz,jz)
        INPUT:
           Either:
              a) R,vR,vT,z,vz:
                 1) floats: phase-space value for single object
                 2) numpy.ndarray: [N] phase-space values for N objects 
                 3) numpy.ndarray: [N,M] phase-space values for N objects at M
                    times
              b) Orbit instance or list thereof; can be integrated already
           nonaxi= set to True to also calculate Lz using the isochrone 
                   approximation for non-axisymmetric potentials
           cumul= if True, return the cumulative average actions (to look 
                  at convergence)
        OUTPUT:
           (jr,lz,jz)
        HISTORY:
           2013-09-10 - Written - Bovy (IAS)
        """
        R,vR,vT,z,vz,phi= self._parse_args(False,*args)
        if self._c:
            pass
        else:
            #Use self._aAI to calculate the actions and angles in the isochrone potential
            acfs= self._aAI.actionsFreqsAngles(R.flatten(),
                                               vR.flatten(),
                                               vT.flatten(),
                                               z.flatten(),
                                               vz.flatten(),
                                               phi.flatten())
            jrI= nu.reshape(acfs[0],R.shape)[:,:-1]
            jzI= nu.reshape(acfs[2],R.shape)[:,:-1]
            anglerI= nu.reshape(acfs[6],R.shape)
            anglezI= nu.reshape(acfs[8],R.shape)
            danglerI= ((nu.roll(anglerI,-1,axis=1)-anglerI) % _TWOPI)[:,:-1]
            danglezI= ((nu.roll(anglezI,-1,axis=1)-anglezI) % _TWOPI)[:,:-1]
            if kwargs.has_key('cumul') and kwargs['cumul']:
                sumFunc= nu.cumsum
            else:
                sumFunc= nu.sum
            jr= sumFunc(jrI*danglerI,axis=1)/sumFunc(danglerI,axis=1)
            jz= sumFunc(jzI*danglezI,axis=1)/sumFunc(danglezI,axis=1)
            if kwargs.has_key('nonaxi') and kwargs['nonaxi']:
                lzI= nu.reshape(acfs[1],R.shape)[:,:-1]
                anglephiI= nu.reshape(acfs[7],R.shape)
                danglephiI= ((nu.roll(anglephiI,-1,axis=1)-anglephiI) % _TWOPI)[:,:-1]
                lz= sumFunc(lzI*danglephiI,axis=1)/sumFunc(danglephiI,axis=1)
            else:
                lz= R[:,0]*vT[:,0]
            return (jr,lz,jz)

    def actionsFreqs(self,*args,**kwargs):
        """
        NAME:
           actionsFreqs
        PURPOSE:
           evaluate the actions and frequencies (jr,lz,jz,Omegar,Omegaphi,Omegaz)
        INPUT:
           Either:
              a) R,vR,vT,z,vz:
                 1) floats: phase-space value for single object
                 2) numpy.ndarray: [N] phase-space values for N objects 
                 3) numpy.ndarray: [N,M] phase-space values for N objects at M
                    times
              b) Orbit instance or list thereof; can be integrated already
           nonaxi= set to True to also calculate Lz using the isochrone 
                   approximation for non-axisymmetric potentials
        OUTPUT:
            (jr,lz,jz,Omegar,Omegaphi,Omegaz)
        HISTORY:
           2013-09-10 - Written - Bovy (IAS)
        """
        acfs= self.actionsFreqsAngles(*args,**kwargs)
        return (acfs[0],acfs[1],acfs[2],acfs[3],acfs[4],acfs[5])

    def actionsFreqsAngles(self,*args,**kwargs):
        """
        NAME:
           actionsFreqsAngles
        PURPOSE:
           evaluate the actions, frequencies, and angles 
           (jr,lz,jz,Omegar,Omegaphi,Omegaz,angler,anglephi,anglez)
        INPUT:
           Either:
              a) R,vR,vT,z,vz:
                 1) floats: phase-space value for single object
                 2) numpy.ndarray: [N] phase-space values for N objects 
                 3) numpy.ndarray: [N,M] phase-space values for N objects at M
                    times
              b) Orbit instance or list thereof; can be integrated already
           maxn= (default: 3) Use a grid in vec(n) up to this n (zero-based)
           nonaxi= set to True to also calculate Lz using the isochrone 
                   approximation for non-axisymmetric potentials
           ts= if set, the phase-space points correspond to these times (IF NOT SET, WE ASSUME THAT ts IS THAT THAT IS ASSOCIATED WITH THIS OBJECT)
        OUTPUT:
            (jr,lz,jz,Omegar,Omegaphi,Omegaz,angler,anglephi,anglez)
        HISTORY:
           2013-09-10 - Written - Bovy (IAS)
        """
        R,vR,vT,z,vz,phi= self._parse_args(True,*args)
        if kwargs.has_key('ts'):
            ts= kwargs['ts']
        else:
            ts= nu.empty(R.shape[1])
            ts[self._ntintJ-1:]= self._tsJ
            ts[:self._ntintJ-1]= -self._tsJ[1:][::-1]
        if kwargs.has_key('maxn'):
            maxn= kwargs['maxn']
        else:
            maxn= 3
        if self._c:
            pass
        else:
            #Use self._aAI to calculate the actions and angles in the isochrone potential
            acfs= self._aAI.actionsFreqsAngles(R.flatten(),
                                               vR.flatten(),
                                               vT.flatten(),
                                               z.flatten(),
                                               vz.flatten(),
                                               phi.flatten())
            jrI= nu.reshape(acfs[0],R.shape)[:,:-1]
            jzI= nu.reshape(acfs[2],R.shape)[:,:-1]
            anglerI= nu.reshape(acfs[6],R.shape)
            anglezI= nu.reshape(acfs[8],R.shape)
            danglerI= ((nu.roll(anglerI,-1,axis=1)-anglerI) % _TWOPI)[:,:-1]
            danglezI= ((nu.roll(anglezI,-1,axis=1)-anglezI) % _TWOPI)[:,:-1]
            if kwargs.has_key('cumul') and kwargs['cumul']:
                sumFunc= nu.cumsum
            else:
                sumFunc= nu.sum
            jr= sumFunc(jrI*danglerI,axis=1)/sumFunc(danglerI,axis=1)
            jz= sumFunc(jzI*danglezI,axis=1)/sumFunc(danglezI,axis=1)
            if kwargs.has_key('nonaxi') and kwargs['nonaxi']:
                lzI= nu.reshape(acfs[1],R.shape)[:,:-1]
                anglephiI= nu.reshape(acfs[7],R.shape)
                danglephiI= ((nu.roll(anglephiI,-1,axis=1)-anglephiI) % _TWOPI)[:,:-1]
                lz= sumFunc(lzI*danglephiI,axis=1)/sumFunc(danglephiI,axis=1)
            else:
                lz= R[:,len(ts)/2]*vT[:,len(ts)/2]
            #Now do an 'angle-fit'
            angleRT= dePeriod(nu.reshape(acfs[6],R.shape))
            acfs7= nu.reshape(acfs[7],R.shape)
            negFreqIndx= nu.median(acfs7-nu.roll(acfs7,1,axis=1),axis=1) < 0. #anglephi is decreasing
            anglephiT= nu.empty(acfs7.shape)
            anglephiT[negFreqIndx,:]= dePeriod(_TWOPI-acfs7[negFreqIndx,:])
            negFreqPhi= nu.zeros(R.shape[0],dtype='bool')
            negFreqPhi[negFreqIndx]= True
            anglephiT[True-negFreqIndx,:]= dePeriod(acfs7[True-negFreqIndx,:])
            angleZT= dePeriod(nu.reshape(acfs[8],R.shape))
            #Write the angle-fit as Y=AX, build A and Y
            nt= len(ts)
            no= R.shape[0]
            nn= maxn*(2*maxn-1)-maxn #remove 0,0,0
            A= nu.zeros((no,nt,2+nn))
            A[:,:,0]= 1.
            A[:,:,1]= ts
            #sorting the phi and Z grids this way makes it easy to exclude the origin
            phig= list(nu.arange(-maxn+1,maxn,1))
            phig.sort(key = lambda x: abs(x))
            phig= nu.array(phig,dtype='int')
            grid= nu.meshgrid(nu.arange(maxn),
                              phig,
                              indexing='ij')
            gridR= grid[0].flatten()[1:] #remove 0,0,0
            gridZ= grid[1].flatten()[1:]
            mask = nu.ones(len(gridR),dtype=bool)
            mask[:2*maxn-3:2]= False
            gridR= gridR[mask]
            gridZ= gridZ[mask]
            tangleR= nu.tile(angleRT.T,(nn,1,1)).T
            tgridR= nu.tile(gridR,(no,nt,1))
            tangleZ= nu.tile(angleZT.T,(nn,1,1)).T
            tgridZ= nu.tile(gridZ,(no,nt,1))
            sinnR= nu.sin(tgridR*tangleR+tgridZ*tangleZ)
            A[:,:,2:]= sinnR
            #Matrix magic
            atainv= nu.empty((no,2+nn,2+nn))
            AT= nu.transpose(A,axes=(0,2,1))
            for ii in range(no):
                atainv[ii,:,:,]= linalg.inv(nu.dot(AT[ii,:,:],A[ii,:,:]))
            ATAR= nu.sum(AT*nu.transpose(nu.tile(angleRT,(2+nn,1,1)),axes=(1,0,2)),axis=2)
            ATAT= nu.sum(AT*nu.transpose(nu.tile(anglephiT,(2+nn,1,1)),axes=(1,0,2)),axis=2)
            ATAZ= nu.sum(AT*nu.transpose(nu.tile(angleZT,(2+nn,1,1)),axes=(1,0,2)),axis=2)
            angleR= nu.sum(atainv[:,0,:]*ATAR,axis=1)
            OmegaR= nu.sum(atainv[:,1,:]*ATAR,axis=1)
            anglephi= nu.sum(atainv[:,0,:]*ATAT,axis=1)
            Omegaphi= nu.sum(atainv[:,1,:]*ATAT,axis=1)
            angleZ= nu.sum(atainv[:,0,:]*ATAZ,axis=1)
            OmegaZ= nu.sum(atainv[:,1,:]*ATAZ,axis=1)
            Omegaphi[negFreqIndx]= -Omegaphi[negFreqIndx]
            anglephi[negFreqIndx]= _TWOPI-anglephi[negFreqIndx]
            return (jr,lz,jz,OmegaR,Omegaphi,OmegaZ,
                    angleR % _TWOPI,
                    anglephi % _TWOPI,
                    angleZ % _TWOPI)


    def _parse_args(self,freqsAngles=True,*args):
        """Helper function to parse the arguments to the __call__ and actionsFreqsAngles functions"""
        RasOrbit= False
        if len(args) == 5:
            raise IOError("Must specify phi for actionAngleIsochroneApprox")
        if len(args) == 6:
            R,vR,vT, z, vz, phi= args
            if isinstance(R,float):
                o= Orbit([R,vR,vT,z,vz,phi])
                o.integrate(self._tsJ,pot=self._pot,method=self._integrate_method)
                this_orbit= o.getOrbit()
                R= nu.reshape(this_orbit[:,0],(1,self._ntintJ))
                vR= nu.reshape(this_orbit[:,1],(1,self._ntintJ))
                vT= nu.reshape(this_orbit[:,2],(1,self._ntintJ))
                z= nu.reshape(this_orbit[:,3],(1,self._ntintJ))
                vz= nu.reshape(this_orbit[:,4],(1,self._ntintJ))           
                phi= nu.reshape(this_orbit[:,5],(1,self._ntintJ))           
            if len(R.shape) == 1: #not integrated yet
                os= [Orbit([R[ii],vR[ii],vT[ii],z[ii],vz[ii],phi[ii]]) for ii in range(R.shape[0])]
                RasOrbit= True
        if isinstance(args[0],Orbit) \
                or (isinstance(args[0],list) and isinstance(args[0][0],Orbit)) \
                or RasOrbit:
            if RasOrbit:
                pass
            elif not isinstance(args[0],list):
                os= [args[0]]
            else:
                os= args[0]
            if not hasattr(os[0],'orbit'): #not integrated yet
                [o.integrate(self._tsJ,pot=self._pot,
                             method=self._integrate_method) for o in os]
            ntJ= os[0].getOrbit().shape[0]
            no= len(os)
            R= nu.empty((no,ntJ))
            vR= nu.empty((no,ntJ))
            vT= nu.empty((no,ntJ))
            z= nu.empty((no,ntJ))
            vz= nu.empty((no,ntJ))
            phi= nu.empty((no,ntJ))
            for ii in range(len(os)):
                this_orbit= os[ii].getOrbit()
                R[ii,:]= this_orbit[:,0]
                vR[ii,:]= this_orbit[:,1]
                vT[ii,:]= this_orbit[:,2]
                z[ii,:]= this_orbit[:,3]
                vz[ii,:]= this_orbit[:,4]
                phi[ii,:]= this_orbit[:,5]
        if freqsAngles: #also integrate backwards in time, such that the requested point is not at the edge
            no= R.shape[0]
            nt= R.shape[1]
            oR= nu.empty((no,2*nt-1))
            ovR= nu.empty((no,2*nt-1))
            ovT= nu.empty((no,2*nt-1))
            oz= nu.empty((no,2*nt-1))
            ovz= nu.empty((no,2*nt-1))
            ophi= nu.empty((no,2*nt-1))
            oR[:,nt-1:]= R
            ovR[:,nt-1:]= vR
            ovT[:,nt-1:]= vT
            oz[:,nt-1:]= z
            ovz[:,nt-1:]= vz
            ophi[:,nt-1:]= phi
            #load orbits
            os= [Orbit([R[ii,0],-vR[ii,0],-vT[ii,0],z[ii,0],-vz[ii,0],phi[ii,0]]) for ii in range(R.shape[0])]
            #integrate orbits
            [o.integrate(self._tsJ,pot=self._pot,
                         method=self._integrate_method) for o in os]
            #extract phase-space points along the orbit
            ts= self._tsJ
            for ii in range(no):
                oR[ii,:nt-1]= os[ii].R(ts[1:])[::-1] #drop t=0, which we have
                ovR[ii,:nt-1]= -os[ii].vR(ts[1:])[::-1] #already
                ovT[ii,:nt-1]= -os[ii].vT(ts[1:])[::-1] # reverse, such that 
                oz[ii,:nt-1]= os[ii].z(ts[1:])[::-1] #everything is in the 
                ovz[ii,:nt-1]= -os[ii].vz(ts[1:])[::-1] #right order
                ophi[ii,:nt-1]= os[ii].phi(ts[1:])[::-1] #!
            return (oR,ovR,ovT,oz,ovz,ophi)
        else:
            return (R,vR,vT,z,vz,phi)

def estimateBIsochrone(R,z,pot=None):
    """
    NAME:
       estimateBIsochrone
    PURPOSE:
       Estimate a good value for the scale of the isochrone potential by matching the slope of the rotation curve
    INPUT:
       R,z = coordinates (if these are arrays, the median estimated delta is returned, i.e., if this is an orbit)
       pot= Potential instance or list thereof
    OUTPUT:
       b if 1 R,Z given
       bmin,bmedian,bmax if multiple R given       
    HISTORY:
       2013-09-12 - Written - Bovy (IAS)
    """
    if pot is None:
        raise IOError("pot= needs to be set to a Potential instance or list thereof")
    if isinstance(R,nu.ndarray):
        bs= nu.array([estimateBIsochrone(R[ii],z[ii],pot=pot) for ii in range(len(R))])
        return (nu.amin(bs[True-nu.isnan(bs)]),
                nu.median(bs[True-nu.isnan(bs)]),
                nu.amax(bs[True-nu.isnan(bs)]))
    else:
        r2= R**2.+z**2
        r= math.sqrt(r2)
        dlvcdlr= dvcircdR(pot,r)/vcirc(pot,r)*r
        try:
            b= optimize.brentq(lambda x: dlvcdlr-(x/math.sqrt(r2+x**2.)-0.5*r2/(r2+x**2.)),
                               0.01,100.)
        except:
            b= nu.nan
        return b

def dePeriod(arr):
    """make an array of periodic angles increase linearly"""
    diff= arr-nu.roll(arr,1,axis=1)
    w= diff < -6.
    addto= nu.cumsum(w.astype(int),axis=1)
    return arr+_TWOPI*addto
