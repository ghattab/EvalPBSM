# Evaluation Physics Based Shape Matching (PBSM) approach
This repository contains data, source, and results from using the physics-based shape matching or PBSM algorithm on ground truth _in silico_ and experimental phantom liver models, respectively.

## Data
Suwelack S, Röhl S, Bodenstedt S, Reichard D, Dillmann R, Santos T, Maier‐Hein L, Wagner M, Wünscher J, Kenngott H, Müller BP. Physics‐based shape matching for intraoperative image guidance. Medical physics. 2014 Nov 1;41(11). [Data](http://opencas.webarchiv.kit.edu/?q=PhysicsBasedShapeMatching "Download link") from the Open-CAS: Validating and Benchmarking Computer Assisted Surgery.

## PBSM approach
The employed PBSM approach is a SOFA based implementation of the PBSM approach.
The implementation uses the Medical Simulation Markup Language (MSML) and is available as a docker container.

### Install docker container
The PBSM approach used for the evaluation is available as a Docker [container](https://github.com/ssuwelack/msml-docker-runtime).
1. Install the Docker framework for your Linux distribution. Further details can be found on the Docker homepage. For Ubuntu Linux there is the possibility to use either [pre-configured](www.ubuntuupdates.org/ppa/docker) packages or run a [manual](http://docs.docker.com/installation/ubuntulinux/) installation
2. To avoid the use of `sudo` in front of the docker commands, you may grant access to a user using: `$ sudo usermod −aG docker username` (Log out for the changes to take effect)
3. Pull the SOFA container from the Docker Hub using: `$ docker pull ssuwelack/msml_sofa` or clone it from Github using `$ git clone https://github.com/ssuwelack/msml−docker−runtime.git`.

### Run container
There are two different options to run a graphical application inside the simulation container.
Either start an SSH server inside the container and connect to it, or link the host X-server into the container. 
Both start-up procedures are available as shell scripts from the aforementioned Github repository, e.g. `$ ./ run_msml_sofa.sh`.
When prompted for a user and password, use `msml` for both.
For linux clients, you may also run the container as a server and connect to it with an instance using `$ ssh −XC msml@servername −p portnumber`.
The recommended approach is communicating over SSH. It is described in four steps:
1. `$ docker run −d −p 127.0.0.1:22000:22 −−name msml_sofa ssuwelack/msml_sofa/root/start_ssh.sh`
2. `$ ./ start_ssh_msml_sofa.sh`
3. `$ ssh −XC msml@localhost −p 22000` (alternative usage using the user/pwd msml)
4. The docker name is `msml_sofa` and is responsive to `docker start/stop/rm` commands.

### PBSM using MSML
The interfacing is Python and XML based.
In the docker, the python script example can be found in 
`/examples/PythonExamples/LiverShapeMatching/Shape- MatchingRunner.py`
In order to run this example from the command line, the MSML source should be in the Python path:
`$ export PYTHONPATH="$PYTHONPATH:/opt/msml/src`.
Then move inside the folder that contains the script
`$ cd /opt/msml/examples/PythonExamples/LiverShapeMatching` and run `$ python ShapeMatchingRunner.py`.
Example `.py` and `.xml` files are provided for the Delaunay triangulation and coupled optimization mesh in the `src` folder.

## Evaluation
Once the volume is registered to the target surface. The surface mesh of the deformed volume is extracted (VTK/Paraview).
It is then voxelized using [Binvox](https://www.patrickmin.com/binvox/) creating a grid size of 1024^3.
Example run:
`./binvox -d 1024 -t vtk path-to-stl-file`

The voxelized volumes are compared against the full surface registration using [Visceral](https://github.com/Visceral-Project/EvaluateSegmentation).
Example run: `./EvaluateGrids path-to-deformed-ground-truth-voxelized-vtk-file path-to-deformed-test-voxelized-vtk-file -use qll -unit millimiter/voxel > output-path.txt` 
Both executables are reported in the source folder `src`.
All results are reported in the `res` folder in each setting (either _in silico_ or phantom experiment).

