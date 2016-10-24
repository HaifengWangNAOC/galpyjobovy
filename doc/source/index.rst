.. galpy documentation master file, created by
   sphinx-quickstart on Sun Jul 11 15:58:27 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. ifconfig:: not_on_rtd

   .. WARNING:: You are looking at the rarely updated, GitHub version of this documentation, **please go to** `galpy.readthedocs.io <http://galpy.readthedocs.io>`_ **for the latest documentation**.

Welcome to galpy's documentation
=================================

galpy is a Python 2 and 3 package for galactic dynamics. It supports
orbit integration in a variety of potentials, evaluating and sampling
various distribution functions, and the calculation of action-angle
coordinates for all static potentials. galpy is an `astropy
<http://www.astropy.org/>`_ `affiliated package
<http://www.astropy.org/affiliated/>`_ and provides full support for
astropy's `Quantity
<http://docs.astropy.org/en/stable/api/astropy.units.Quantity.html>`_
framework for variables with units.

Quick-start guide
-----------------

.. toctree::
   :maxdepth: 2

   installation.rst

   whatsnew.rst

   getting_started.rst

   potential.rst

   basic_df.rst

   orbit.rst

   actionAngle.rst

   diskdf.rst

Tutorials
---------

.. toctree::
   :maxdepth: 2

   streamdf.rst

Library reference
-----------------

.. toctree::
   :maxdepth: 2

   reference/orbit.rst

   reference/potential.rst

   reference/aa.rst

   reference/df.rst

   reference/util.rst


Acknowledging galpy
--------------------

If you use galpy in a publication, please cite the following paper

* *galpy: A Python Library for Galactic Dynamics*, Jo Bovy (2015), *Astrophys. J. Supp.*, **216**, 29 (`arXiv/1412.3451 <http://arxiv.org/abs/1412.3451>`_).

and link to ``http://github.com/jobovy/galpy``. Some of the code's
functionality is introduced in separate papers (like
``galpy.df.streamdf`` and ``galpy.df.streamgapdf``, see below), so
please also cite those papers when using these functions. Please also
send me a reference to the paper or send a pull request including your
paper in the list of galpy papers on this page (this page is at
doc/source/index.rst). Thanks!

When using the ``galpy.actionAngle.actionAngleAdiabatic`` and ``galpy.actionAngle.actionAngleStaeckel`` modules, please cite `2013ApJ...779..115B <http://adsabs.harvard.edu/abs/2013ApJ...779..115B>`_ in addition to the papers describing the algorithm used. When using ``galpy.actionAngle.actionAngleIsochroneApprox``, please cite `2014ApJ...795...95B <http://adsabs.harvard.edu/abs/2014ApJ...795...95B>`_, which introduced this technique.


Papers using galpy
--------------------

``galpy`` is described in detail in this publication:

* *galpy: A Python Library for Galactic Dynamics*, Jo Bovy (2015), *Astrophys. J. Supp.*, **216**, 29 (`2015ApJS..216...29B <http://adsabs.harvard.edu/abs/2015ApJS..216...29B>`_).

The following is a list of publications using ``galpy``; please let me (bovy at astro dot utoronto dot ca) know if you make use of ``galpy`` in a publication.

#. *Tracing the Hercules stream around the Galaxy*, Jo Bovy (2010), *Astrophys. J.* **725**, 1676 (`2010ApJ...725.1676B <http://adsabs.harvard.edu/abs/2010ApJ...725.1676B>`_): 
  	   Uses what later became the orbit integration routines and Dehnen and Shu disk distribution functions.
#. *The spatial structure of mono-abundance sub-populations of the Milky Way disk*, Jo Bovy, Hans-Walter Rix, Chao Liu, et al. (2012), *Astrophys. J.* **753**, 148 (`2012ApJ...753..148B <http://adsabs.harvard.edu/abs/2012ApJ...753..148B>`_):
       Employs galpy orbit integration in ``galpy.potential.MWPotential`` to characterize the orbits in the SEGUE G dwarf sample.
#. *On the local dark matter density*, Jo Bovy & Scott Tremaine (2012), *Astrophys. J.* **756**, 89 (`2012ApJ...756...89B <http://adsabs.harvard.edu/abs/2012ApJ...756...89B>`_):
      Uses ``galpy.potential`` force and density routines to characterize the difference between the vertical force and the surface density at large heights above the MW midplane.
#. *The Milky Way's circular velocity curve between 4 and 14 kpc from APOGEE data*, Jo Bovy, Carlos Allende Prieto, Timothy C. Beers, et al. (2012), *Astrophys. J.* **759**, 131 (`2012ApJ...759..131B <http://adsabs.harvard.edu/abs/2012ApJ...759..131B>`_):
       Utilizes the Dehnen distribution function to inform a simple model of the velocity distribution of APOGEE stars in the Milky Way disk and to create mock data.
#. *A direct dynamical measurement of the Milky Way's disk surface density profile, disk scale length, and dark matter profile at 4 kpc < R < 9 kpc*, Jo Bovy & Hans-Walter Rix (2013), *Astrophys. J.* **779**, 115 (`2013ApJ...779..115B <http://adsabs.harvard.edu/abs/2013ApJ...779..115B>`_):
     Makes use of potential models, the adiabatic and Staeckel actionAngle modules, and the quasiisothermal DF to model the dynamics of the SEGUE G dwarf sample in mono-abundance bins.
#. *The peculiar pulsar population of the central parsec*, Jason Dexter & Ryan M. O'Leary (2013), *Astrophys. J. Lett.*, **783**, L7 (`2014ApJ...783L...7D <http://adsabs.harvard.edu/abs/2014ApJ...783L...7D>`_):
     Uses galpy for orbit integration of pulsars kicked out of the Galactic center.
#. *Chemodynamics of the Milky Way. I. The first year of APOGEE data*, Friedrich Anders, Christina Chiappini, Basilio X. Santiago, et al. (2013), *Astron. & Astrophys.*, **564**, A115 (`2014A&A...564A.115A <http://adsabs.harvard.edu/abs/2014A%26A...564A.115A>`_):
  		 Employs galpy to perform orbit integrations in ``galpy.potential.MWPotential`` to characterize the orbits of stars in the APOGEE sample.

#. *Dynamical modeling of tidal streams*, Jo Bovy (2014), *Astrophys. J.*, **795**, 95 (`2014ApJ...795...95B <http://adsabs.harvard.edu/abs/2014ApJ...795...95B>`_):
    Introduces ``galpy.df.streamdf`` and ``galpy.actionAngle.actionAngleIsochroneApprox`` for modeling tidal streams using simple models formulated in action-angle space (see the tutorial above).
#. *The Milky Way Tomography with SDSS. V. Mapping the Dark Matter Halo*, Sarah R. Loebman, Zeljko Ivezic Thomas R. Quinn, Jo Bovy, Charlotte R. Christensen, Mario Juric, Rok Roskar, Alyson M. Brooks, & Fabio Governato (2014), *Astrophys. J.*, **794**, 151 (`2014ApJ...794..151L <http://adsabs.harvard.edu/abs/2014ApJ...794..151L>`_):
    Uses ``galpy.potential`` functions to calculate the acceleration field of the best-fit potential in Bovy & Rix (2013) above.
#. *The Proper Motion of the Galactic Center Pulsar Relative to Sagittarius A**, Geoffrey C. Bower, Adam Deller, Paul Demorest, et al. (2015), *Astrophys. J.*, **798**, 120 (`2015ApJ...798..120B <http://adsabs.harvard.edu/abs/2015ApJ...798..120B>`_):
    Utilizes ``galpy.orbit`` integration in Monte Carlo simulations of the possible origin of the pulsar PSR J1745-2900 near the black hole at the center of the Milky Way.
#. *The power spectrum of the Milky Way: Velocity fluctuations in the Galactic disk*, Jo Bovy, Jonathan C. Bird, Ana E. Garcia Perez, Steven M. Majewski, David L. Nidever, & Gail Zasowski (2015), *Astrophys. J.*, **800**, 83 (`2015ApJ...800...83B <http://adsabs.harvard.edu/abs/2015ApJ...800...83B>`_):
    Uses ``galpy.df.evolveddiskdf`` to calculate the mean non-axisymmetric velocity field due to different non-axisymmetric perturbations and compares it to APOGEE data.
#. *The LMC geometry and outer stellar populations from early DES data*, Eduardo Balbinot, B. X. Santiago, L. Girardi, et al. (2015), *Mon. Not. Roy. Astron. Soc.*, **449**, 1129 (`2015MNRAS.449.1129B <http://adsabs.harvard.edu/abs/2015MNRAS.449.1129B>`_):
    Employs ``galpy.potential.MWPotential`` as a mass model for the Milky Way to constrain the mass of the LMC.
#. *Generation of mock tidal streams*, Mark A. Fardal, Shuiyao Huang, & Martin D. Weinberg (2015), *Mon. Not. Roy. Astron. Soc.*, **452**, 301 (`2015MNRAS.452..301F <http://adsabs.harvard.edu/abs/2015MNRAS.452..301F>`_):
    Uses ``galpy.potential`` and ``galpy.orbit`` for orbit integration in creating a *particle-spray* model for tidal streams.
#. *The nature and orbit of the Ophiuchus stream*, Branimir Sesar, Jo Bovy, Edouard J. Bernard, et al. (2015), *Astrophys. J.*, **809**, 59 (`2015ApJ...809...59S <http://adsabs.harvard.edu/abs/2015ApJ...809...59S>`_):
    Uses the ``Orbit.fit`` routine in ``galpy.orbit`` to fit the orbit of the Ophiuchus stream to newly obtained observational data and the routines in ``galpy.df.streamdf`` to model the creation of the stream.
#. *Young Pulsars and the Galactic Center GeV Gamma-ray Excess*, Ryan M. O'Leary, Matthew D. Kistler, Matthew Kerr, & Jason Dexter (2015), *Phys. Rev. Lett.*, submitted (`arXiv/1504.02477 <http://arxiv.org/abs/1504.02477>`_):
     Uses galpy orbit integration  and ``galpy.potential.MWPotential2014`` as part of a Monte Carlo simulation of the Galactic young-pulsar population.
#. *Phase Wrapping of Epicyclic Perturbations in the Wobbly Galaxy*, Alexander de la Vega, Alice C. Quillen, Jeffrey L. Carlin, Sukanya Chakrabarti, & Elena D'Onghia (2015), *Mon. Not. Roy. Astron. Soc.*, **454**, 933 (`2015MNRAS.454..933D <http://adsabs.harvard.edu/abs/2015MNRAS.454..933D>`_):
     Employs galpy orbit integration, ``galpy.potential`` functions, and ``galpy.potential.MWPotential2014`` to investigate epicyclic motions induced by the pericentric passage of a large dwarf galaxy and how these motions give rise to streaming motions in the vertical velocities of Milky Way disk stars.
#. *Chemistry of the Most Metal-poor Stars in the Bulge and the z ≳ 10 Universe*, Andrew R. Casey & Kevin C. Schlaufman (2015), *Astrophys. J.*, **809**, 110 (`2015ApJ...809..110C <http://adsabs.harvard.edu/abs/2015ApJ...809..110C>`_):
     This paper employs galpy orbit integration in ``MWPotential`` to characterize the orbits of three very metal-poor stars in the Galactic bulge.
#. *The Phoenix stream: a cold stream in the Southern hemisphere*, E. Balbinot, B. Yanny, T. S. Li, et al. (2015), *Astrophys. J.*, **820**, 58 (`2016ApJ...820...58B <http://adsabs.harvard.edu/abs/2016ApJ...820...58B>`_).
#. *Discovery of a Stellar Overdensity in Eridanus-Phoenix in the Dark Energy Survey*, T. S. Li, E. Balbinot, N. Mondrik, et al. (2015), *Astrophys. J.*, **817**, 135 (`2016ApJ...817..135L <http://adsabs.harvard.edu/abs/2016ApJ...817..135L>`_):
     Both of these papers use galpy orbit integration to integrate the orbit of NGC 1261 to investigate a possible association of this cluster with the newly discovered Phoenix stream and Eridanus-Phoenix overdensity.
#. *The Proper Motion of Palomar 5*, T. K. Fritz & N. Kallivayalil (2015), *Astrophys. J.*, **811**, 123 (`2015ApJ...811..123F <http://adsabs.harvard.edu/abs/2015ApJ...811..123F>`_):
     This paper makes use of the ``galpy.df.streamdf`` model for tidal streams to constrain the Milky Way's gravitational potential using the kinematics of the Palomar 5 cluster and stream.
#. *Spiral- and bar-driven peculiar velocities in Milky Way-sized galaxy simulations*, Robert J. J. Grand, Jo Bovy, Daisuke Kawata, Jason A. S. Hunt, Benoit Famaey, Arnaud Siebert, Giacomo Monari, & Mark Cropper (2015), *Mon. Not. Roy. Astron. Soc.*, **453**, 1867 (`2015MNRAS.453.1867G <http://adsabs.harvard.edu/abs/2015MNRAS.453.1867G>`_):
     Uses ``galpy.df.evolveddiskdf`` to calculate the mean non-axisymmetric velo\city field due to the bar in different parts of the Milky Way.
#. *Vertical kinematics of the thick disc at 4.5 ≲ R ≲ 9.5 kpc*, Kohei Hattori & Gerard Gilmore (2015), *Mon. Not. Roy. Astron. Soc.*, **454**, 649 (`2015MNRAS.454..649H <http://adsabs.harvard.edu/abs/2015MNRAS.454..649H>`_):
     This paper uses ``galpy.potential`` functions to set up a realistic Milky-Way potential for investigating the kinematics of stars in the thick disk.
#. *Local Stellar Kinematics from RAVE data - VI. Metallicity Gradients Based on the F-G Main-sequence Stars*, O. Plevne, T. Ak, S. Karaali, S. Bilir, S. Ak, Z. F. Bostanci (2015), *Pub. Astron. Soc. Aus.*, **32**, 43 (`2015PASA...32...43P <http://adsabs.harvard.edu/abs/2015PASA...32...43P>`_):
     This paper employs galpy orbit integration in ``MWPotential2014`` to calculate orbital parameters for a sample of RAVE F and G dwarfs to investigate the metallicity gradient in the Milky Way.
#. *Dynamics of stream-subhalo interactions*, Jason L. Sanders, Jo Bovy, & Denis Erkal (2015), *Mon. Not. Roy. Astron. Soc.*, **457**, 3817 (`2016MNRAS.457.3817S <http://adsabs.harvard.edu/abs/2016MNRAS.457.3817S>`_):
     Uses and extends ``galpy.df.streamdf`` to build a generative model of the dynamical effect of sub-halo impacts on tidal streams. This new functionality is contained in ``galpy.df.streamgapdf``, a subclass of ``galpy.df.streamdf``, and can be used to efficiently model the effect of impacts on the present-day structure of streams in position and velocity space.
#. *Extremely metal-poor stars from the cosmic dawn in the bulge of the Milky Way*, L. M. Howes, A. R. Casey, M. Asplund, et al. (2015), *Nature*, **527**, 484 (`2015Natur.527..484H <http://adsabs.harvard.edu/abs/2015Natur.527..484H>`_):
     Employs galpy orbit integration in ``MWPotential2014`` to characterize the orbits of a sample of extremely metal-poor stars found in the bulge of the Milky Way. This analysis demonstrates that the orbits of these metal-poor stars are always close to the center of the Milky Way and that these stars are therefore true bulge stars rather than halo stars passing through the bulge.
#. *Detecting the disruption of dark-matter halos with stellar streams*, Jo Bovy (2016), *Phys. Rev. Lett.*, **116**, 121301 (`2016PhRvL.116l1301B <http://adsabs.harvard.edu/abs/2016PhRvL.116l1301B>`_):
     Uses galpy functions in ``galpy.df`` to estimate the velocity kick imparted by a disrupting dark-matter halo on a stellar stream. Also employs ``galpy.orbit`` integration and ``galpy.actionAngle`` functions to analyze *N*-body simulations of such an interaction.
#. *Identification of Globular Cluster Stars in RAVE data II: Extended tidal debris around NGC 3201*, B. Anguiano, G. M. De Silva, K. Freeman, et al. (2016), *Mon. Not. Roy. Astron. Soc.*, **457**, 2078 (`2016MNRAS.457.2078A <http://adsabs.harvard.edu/abs/2016MNRAS.457.2078A>`_):
     Employs ``galpy.orbit`` integration to study the orbits of potential tidal-debris members of NGC 3201.
#. *Young and Millisecond Pulsar GeV Gamma-ray Fluxes from the Galactic Center and Beyond*, Ryan M. O'Leary, Matthew D. Kistler, Matthew Kerr, & Jason Dexter (2016), *Phys. Rev. D*, submitted (`arXiv/1601.05797 <http://arxiv.org/abs/1601.05797>`_):
     Uses ``galpy.orbit`` integration in ``MWPotential2014`` for orbit integration of pulsars kicked out of the central region of the Milky Way.
#. *Abundances and kinematics for ten anticentre open clusters*, T. Cantat-Gaudin, P. Donati, A. Vallenari, R. Sordo, A. Bragaglia, L. Magrini (2016), *Astron. & Astrophys.*, **588**, A120 (`2016A&A...588A.120C <http://adsabs.harvard.edu/abs/2016A%26A...588A.120C>`_):
     Uses ``galpy.orbit`` integration in ``MWPotential2014`` to characterize the orbits of 10 open clusters located toward the Galactic anti-center, finding that the most distant clusters have high-eccentricity orbits.
#. *A Magellanic Origin of the DES Dwarfs*, P. Jethwa, D. Erkal, & V. Belokurov (2016), *Mon. Not. Roy. Astron. Soc.*, **461**, 2212 (`arXiv/1603.04420 <http://arxiv.org/abs/1603.04420>`_):
     Employs the C implementations of ``galpy.potential``\s to compute forces in orbit integrations of the LMC's satellite-galaxy population.
#. *PSR J1024-0719: A Millisecond Pulsar in an Unusual Long-Period Orbit*, D. L. Kaplan, T. Kupfer, D. J. Nice, et al. (2016), *Astrophys. J.*, **826**, 86 (`arXiv/1604.00131 <http://arxiv.org/abs/1604.00131>`_):
#. *A millisecond pulsar in an extremely wide binary system*, C. G. Bassa, G. H. Janssen, B. W. Stappers, et al. (2016), *Mon. Not. Roy. Astron. Soc.*, **460**, 2207 (`arXiv/1604.00129 <http://arxiv.org/abs/1604.00129>`_):
     Both of these papers use ``galpy.orbit`` integration in ``MWPotential2014`` to determine the orbit of the milli-second pulsar PSR J1024−0719, a pulsar in an unusual binary system.
#. *The first low-mass black hole X-ray binary identified in quiescence outside of a globular cluster*, B. E. Tetarenko, A. Bahramian, R. M. Arnason, et al. (2016), *Astrophys. J.*, **825**, 10 (`arXiv/1605.00270 <http://arxiv.org/abs/1605.00270>`_):
     This paper employs ``galpy.orbit`` integration of orbits within the position-velocity uncertainty ellipse of the radio source VLA J213002.08+120904 to help characterize its nature (specifically, to rule out that it is a magnetar based on its birth location).
#. *Action-based Dynamical Modelling for the Milky Way Disk*, Wilma H. Trick, Jo Bovy, & Hans-Walter Rix (2016), *Astrophys. J.*, **830**, 97 (`arXiv/1605.08601 <http://arxiv.org/abs/1605.08601>`_):
     Makes use of potential models, the Staeckel actionAngle modules, and the quasiisothermal DF to develop a robust dynamical modeling approach for recovering the Milky Way's gravitational potential from kinematics of disk stars.
#. *A Dipole on the Sky: Predictions for Hypervelocity Stars from the Large Magellanic Cloud*, Douglas Boubert & N. W. Evans (2016), *Astrophys. J. Lett.*, **825**, L6 (`arXiv/1606.02548 <http://arxiv.org/abs/1606.02548>`_):
     Uses ``galpy.orbit`` integration to investigate the orbits of hyper-velocity stars that could be ejected from the Large Magellanic Cloud and their distribution on the sky.
#. *Linear perturbation theory for tidal streams and the small-scale CDM power spectrum*, Jo Bovy, Denis Erkal, & Jason L. Sanders (2016), *Mon. Not. Roy. Astron. Soc.*, submitted (`arXiv/1606.03470 <http://arxiv.org/abs/1606.03470>`_):
     Uses and extends ``galpy.df.streamdf`` and ``galpy.df.streamgapdf`` to quickly compute the effect of impacts from dark-matter subhalos on stellar streams and investigates the structure of perturbed streams and how this structure relates to the CDM subhalo mass spectrum.
#. *Local Stellar Kinematics from RAVE data - VII. Metallicity Gradients from Red Clump Stars*, O. Onal Tas, S. Bilir, G. M. Seabroke, S. Karaali, S. Ak, T. Ak, & Z. F. Bostanci (2016), *Pub. Astron. Soc. Aus.*, **33**, e044 (`arXiv/1607.07049 <http://arxiv.org/abs/1607.07049>`_):
     Employs galpy orbit integration in ``MWPotential2014`` to calculate orbital parameters for a sample of red clump stars in RAVE to investigate the metallicity gradient in the Milky Way.
#. *Study of Eclipsing Binary and Multiple Systems in OB Associations IV: Cas OB6 Member DN Cas*, V. Bakis, H. Bakis, S. Bilir, Z. Eker (2016), *Pub. Astron. Soc. Aus.*, **33**, e046 (`arXiv/1608.00456 <http://arxiv.org/abs/1608.00456>`_):
     Uses galpy orbit integration in ``MWPotential2014`` to calculate the orbit and orbital parameters of the spectroscopic binary DN Cas in the Milky Way.
#. *The shape of the inner Milky Way halo from observations of the Pal 5 and GD-1 stellar streams*, Jo Bovy, Anita Bahmanyar, Tobias K. Fritz, & Nitya Kallivayalil (2016), *Astrophys. J.*, in press (`arXiv/1609.01298 <http://arxiv.org/abs/1609.01298>`_):
     Makes use of the ``galpy.df.streamdf`` model for a tidal stream to constrain the shape and mass of the Milky Way's dark-matter halo. Introduced ``galpy.potential.TriaxialNFWPotential``.
#. *The Rotation-Metallicity Relation for the Galactic Disk as Measured in the Gaia DR1 TGAS and APOGEE Data*, Carlos Allende Prieto, Daisuke Kawata, & Mark Cropper (2016), *Mon. Not. Roy. Astron. Soc.*, submitted (`arXiv/1609.07821 <http://arxiv.org/abs/1609.07821>`_):
     Employs orbit integration in ``MWPotential2014`` to calculate the orbits of a sample of stars in common between Gaia DR1's TGAS and APOGEE to study the rotation-metallicity relation for the Galactic disk.
#. *Detection of a dearth of stars with zero angular momentum in the solar neighbourhood*, Jason A. S. Hunt, Jo Bovy, & Raymond Carlberg (2016), *Astrophys. J.*, submitted (`arXiv/1610.02030 <http://arxiv.org/abs/1610.02030>`_):
     Uses ``galpy.orbit`` integration in ``MWPotential2014`` plus a hard Galactic core to calculate the orbits of stars in the solar neighborhood and predict how many of them should be lost to chaos.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

