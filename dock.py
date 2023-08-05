import os
from vina import Vina
import subprocess
def docking(ligand,receptor, exhaustiveness, n_poses, maps_center, box_size):
    v = Vina(sf_name='vina')
    v.set_receptor(f'{receptor}')

    v.set_ligand_from_file(f'docking_data/ligands/{ligand}.pdbqt')
    v.compute_vina_maps(center=maps_center, box_size=box_size)
    v.dock(exhaustiveness=exhaustiveness, n_poses=n_poses)
    v.write_poses(f'docking_data/docking_result/{ligand}_vina_out.pdbqt', n_poses=n_poses, overwrite=True)
    return v
def prepare_ligand(ligand_list):
    for ligand in ligand_list:
        if os.path.isdir(f"docking_data/ligands/{ligand}.pdbqt"):
            continue
        print('preparing ', ligand)
        command = ["mk_prepare_ligand.py", "-i", f"docking_data/ligands/{ligand}.sdf", "-o", f"docking_data/ligands/{ligand}.pdbqt"]
        subprocess.run(command)
        
        
mainlist = []
with open('docking_data/config.txt','r') as f:
    for i in f.readlines():
        mainlist.append(i)
pdbqt = mainlist[1][:-1]
exhaustiveness = int(mainlist[4][:-1])
grid_spacing = float(mainlist[7][:-1])
grid_1 = (mainlist[10][:-1])
grid_2 = grid_1.split(' ')
grid_ntps = [float(x) for x in grid_2]
grid_3 = (mainlist[13][:-1])
grid_4 = grid_3.split(' ')
grid_center = [float(x) for x in grid_4]
n_poses = int(mainlist[16][:-1])

ligandlist = []
for file_name in os.listdir('docking_data/ligands'):
    if file_name.endswith('.sdf'):
        prepare_ligand([file_name[:-4]])
        input_path = f"data/{file_name}"
        output_path = f"docking_data/docking_result/{os.path.splitext(file_name)[0]}.pdbqt"
    
        result = docking(f'{file_name[:-4]}',pdbqt, exhaustiveness=exhaustiveness, n_poses=n_poses, maps_center=grid_center, box_size=tuple(grid_ntps))

