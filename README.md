# AutoDocker
Automatic Protein-Ligand molecular docking simulation
---------
Requirements:
- python (I used 3.9.12)
- autodockvina
- vina

## Cloning the environment
Download the code or simply run
`git clone https://github.com/erfantoloue/AutoDocker.git`

## Receptor
Convert and clean your PDB receptor structure using AutoDockTools into a PDBQT format and put it in the **receptor** directory. Mention its name in the `config.txt` file.

## Ligands
Download your ligands structures from any chemical databases. The format should be in SDF format and all of them should be in the **ligands** directory. My recommendation is the [ZINC database](https://zinc.docking.org/) which is designed for molecular docking/virutal screening and the ligands are optimized as well.

## Docking parameters
Use AutoDockTools software to determine the exact grid dimensions and grid center for your receptor. This is highly crucial as it will increase the accuracy of the results. <br> <br>
Exhaustiveness refers to the level of thoroughness with which the docking algorithm explores the conformational space of the ligand-receptor complex to search for potential binding poses. <br> <br>
N_poses also refers to the number of poses that you may want for each of the docking results. When docking a lot of ligands into one receptor, I usually put it on 1, so that analyzing the results would be easier.

## Running the code
After finalizing the parameters run <br>
`python dock.py` <br> <br>
It will first turn the first `.sdf` file into a `.pdbqt` file. Consecutively, the ligand will be docked into the receptor. This process will be repeated for each ligand. The docking results will be available in the **docking_result** directory. <br> <br>
Attention: Use a HPC (High Perfomance Computing) unit or a server if you want higher exhaustiveness or if you have a lot of ligands.
