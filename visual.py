from ase.io import read
from espresso import espresso
from ase.optimize import QuasiNewton
from ase.visualize import view
slab_ads=read('Pt+CO.traj')
view(slab_ads)
