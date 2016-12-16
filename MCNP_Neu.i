c                ME_701 Project MCNP Photon File 
c -----------------------------------------------------------------------------
c  ********************** Cell Card *******************************
  1   1   den  -5   3   1   -6   -4   2    imp:N=1 $ Defines Slab 
c  ********************* Vacuum Option ****************************
  99  0   -99   #1 #23                imp:N=1  $ Defines Vacuum Boundaries
c  ******************** Graveyard ****************************
  97  0    99                         imp:N=0  $ Defines Graveyard Boundaries
c *********************** Detectors *******************************
  23  0  -7                           imp:N=1 $ surface detector
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
7   S    50 0 130   2  $ Spherical Detector 1
c 
c **************** Kill Particles/Define Air **********************
c          X-  X+    Y-  Y+   Z-   Z+
99  RPP  -261 261  -261  261  0   300   $ Rectangular Paralleliped (Graveyard)
c -----------------------------------------------------------------------------

c *****************************************************************************
c ------------------------------- DATA CARD -----------------------------------
c *****************************************************************************
SDEF POS=-50 0 130 AXS=0 0 1 PAR=1 ERG=d3      $ Source Term
c                               Energy Bins
SI3  H 0.0 2.5E-8
c                             Probablity Bins
SP3  0.0 1.0
nps 1000000                                             $ Number of Particles
c 
c -----------------------------------------------------------------------------
c ---------------------------- Tally Detectors --------------------------------
c -----------------------------------------------------------------------------
Mode N                                      $ Mode Photon
PHYS:N                                      $ All Photon Types
F2:N 7                        $ Define Tally Surface
FM2 2.981797765E19                          $ Dose Conversion to mrem/h
c 
c -----------------------------------------------------------------------------
c ------------------------------- Materials -----------------------------------
c -----------------------------------------------------------------------------
c                           User Defined Material
M1
c -----------------------------------------------------------------------------
