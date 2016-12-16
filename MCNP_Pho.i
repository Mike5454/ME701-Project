c                ME_701 Project MCNP Photon File 
c -----------------------------------------------------------------------------
c  ********************** Cell Card *******************************
  1   1   den  -5   3   1   -6   -4   2    imp:P=1 $ Defines Slab 
c  ********************* Vacuum Option ****************************
  99  0   -99   #1 #23                imp:P=1  $ Defines Vacuum Boundaries
c  ******************** Graveyard ****************************
  97  0    99                         imp:P=0  $ Defines Graveyard Boundaries
c *********************** Detectors *******************************
  23  0  -7                           imp:P=1 $ surface detector
c -----------------------------------------------------------------------------

c -----------------------------------------------------------------------------
c ******************** Surface Card ** ****************************
c        Define Planes for Concrete Slab
1   PZ     1    $ Bottom Face of Concrete Slab
2   PY   -260   $ Back Face of Concrete Slab
3   PX   -260   $ Left Face of Concrete Slab
4   PY    260   $ Front Face of Concrete Slab
5   PX    260   $ Right Face of Concrete Slab
6   PZ    80    $ Top Face of Concrete Slab
c ********************** Detectors ********************************
c  Type  x y z     R   $ Define Detector Surface
7   S    50 0 50   2  $ Spherical Detector 1
c 
c **************** Kill Particles/Define Air **********************
c          X-  X+    Y-  Y+   Z-   Z+
99  RPP  -261 261  -261  261  0   300   $ Rectangular Paralleliped (Graveyard)
c -----------------------------------------------------------------------------

c -----------------------------------------------------------------------------       
c ********************** Data Card *******************************
c
c ********************** Material ********************************
c                 User Defined Material
c ****************************************************************
M1
c ************************************************************
c ***************** Define Source ********************
c source, position of source, energy of particles, Particle Neutron=1 Photon=2
SDEF POS=-50 0 50 ERG=d1 PAR=2
c d1 will call the lines below for a multi-energetic source
c  
c The following defines our source energies and their respected ratios
SI1 L 0.662 1.25  $ Even though I will use a mono-energetic source this is
SP1     1    0   $ good practice and makes changing source energies quick
c 
c ************** Set Tally Surface ******************
c Define Tally Surface
F995:P  40 0 88 1.26          $ Point Detector for void
c Mode Photon
mode p
c Number of Particles
nps 1000000
c -----------------------------------------------------------------------------
