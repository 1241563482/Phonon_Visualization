import yaml
from ase.io import read, write

band = 15
q_point = 51

poscar = read("POSCAR")
with open('band.yaml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        
vib = data["phonon"][q_point]['band'][0]

elements = poscar.get_chemical_symbols()
atom0 = ""
index = 1

write("mode_qpoint{}_band{}.cif".format(q_point, band), poscar)

str1 = """
loop_
_atom_site_moment_label
_atom_site_moment_crystalaxis_x
_atom_site_moment_crystalaxis_y
_atom_site_moment_crystalaxis_z
"""

with open("mode_qpoint{}_band{}.cif".format(q_point, band), "a") as file:
    print(str1, file = file)
    print(vib)
    for i in range(len(poscar)):
        element = elements[i]
        if element == atom0:
            index = index + 1
            print(element+str(index), vib['eigenvector'][i][0][0], vib['eigenvector'][i][1][0], vib['eigenvector'][i][2][0], file = file)
        else:
            index = 1
            print(element+str(index), vib['eigenvector'][i][0][0], vib['eigenvector'][i][1][0], vib['eigenvector'][i][2][0], file = file)
            atom0 = element

