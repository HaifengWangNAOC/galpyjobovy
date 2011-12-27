import shutil
import tempfile
import pickle
import math
_KMSGYRKPC= 1.0226894377665996
def tphysical(ro=8.,vo=220.):
    return ro/vo/_KMSGYRKPC
def save_pickles(savefilename,*args):
    """
    NAME:
       save_pickles
    PURPOSE:
       relatively safely save things to a pickle
    INPUT:
       savefilename - name of the file to save to; actual save operation will be performed on a temporary file and then that file will be shell mv'ed to savefilename
       +things to pickle (as many as you want!)
    OUTPUT:
       none
    HISTORY:
       2010-? - Written - Bovy (NYU)
       2011-08-23 - generalized and added to galpy.util - Bovy (NYU)
    """
    saving= True
    interrupted= False
    file, tmp_savefilename= tempfile.mkstemp() #savefilename+'.tmp'
    while saving:
        try:
            savefile= open(tmp_savefilename,'wb')
            for f in args:
                pickle.dump(f,savefile)
            savefile.close()
            shutil.move(tmp_savefilename,savefilename)
            saving= False
            if interrupted:
                raise KeyboardInterrupt
        except KeyboardInterrupt:
            if not saving:
                raise
            print "KeyboardInterrupt ignored while saving pickle ..."
            interrupted= True

