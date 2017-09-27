from ase.spacegroup import crystal
from ase.visualize import view
from ase.build import surface
from ase.io import write
from ase.build import molecule
from ase.build import fcc111, add_adsorbate
#build the Pt crystal structure
a=3.923 #angstrom
Pt=crystal(['Pt'],basis=[(0,0,0)],spacegroup=225,cellpar=[a,a,a,90,90,90])

#build the (111) surface slab
Pt_111=surface(Pt,(1,1,1),2)
Pt_111.center(vacuum=10,axis=2)

#repeat slab
Pt_111_repeat=Pt_111.repeat((1,1,1))
#(1,2,1) corresponds to repeat how many times in x,y,z direction
atoms = molecule('CO')
atoms.center(10)
#save .traj file
write('ads_CO.traj',atoms)
write('Pt_111.traj',Pt_111)
view(Pt_111)
add_adsorbate(Pt_111,atoms,1.5)
write('Pt_111+CO.traj',Pt_111)
write('POSCAR',Pt_111) #in case the .traj file cannot be read
view(atoms)
view(Pt_111)

