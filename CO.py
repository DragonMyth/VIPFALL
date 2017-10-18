from ase.build import molecule
from ase.io import write
from ase.visualize import view
atoms=molecule('CO')
atoms.center(10)

#write the .traj file
write('ads_CO.traj',atoms)
#write the POSCAR file incase the .traj file cannot be read
write('POSCAR',atoms)
view(atoms)
