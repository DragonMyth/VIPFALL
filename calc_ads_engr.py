from ase.io import read
from espresso import espresso
from ase.optimize import QuasiNewton

CO_ads=read('opt_ads_CO.traj').get_potential_energy()
Pt_111_ads = read('opt_Pt_111.traj').get_potential_energy()
Pt_CO_ads = read('opt_Pt+CO.traj').get_potential_energy()

print(CO_ads)
print(Pt_111_ads)
print(Pt_CO_ads)

print(Pt_CO_ads-Pt_111_ads-CO_ads)
