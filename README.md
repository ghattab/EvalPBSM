# Evaluation Physics Based Shape Matching (PBSM) approach
This repository contains data, source, and results from using the physics-based shape matching or PBSM algorithm on ground truth _in silico_ and experimental phantom liver models, respectively.

To find out what has the greatest impact on performance, we investigated deformation results using a combination of scenarios: four different tetrahedral meshing algorithms (TETMSH), three different optimization schemes (OPTIM), and six partial target surfaces (bisected from a full Delaunay triangulation). 

## Data
Based on previously published and ground-truth data, we employ the first liver from the _in silico_ validation data and the liver from the phantom experimental data. Suwelack S, Röhl S, Bodenstedt S, Reichard D, Dillmann R, Santos T, Maier‐Hein L, Wagner M, Wünscher J, Kenngott H, Müller BP. Physics‐based shape matching for intraoperative image guidance. Medical physics. 2014 Nov 1;41(11). [Data](http://opencas.webarchiv.kit.edu/?q=PhysicsBasedShapeMatching "Download link") from the Open-CAS: Validating and Benchmarking Computer Assisted Surgery.

## Tetrahedral meshing (TETMSH)
For the scope of this work, we used four TETMSH algorithms: the Delaunay triangulation (DLNY), the Frontal algorithm (FRNTL), the coupled Frontal Delaunay algorithm (FRNTL-DLNY), and the implicit domain mesher (MMG3D). Most of them rely on Tetgen and Netgen algorithms; although both algorithms are characterized as being unstructured algorithms, the created volumes are comparable and are suitable for finite element or FE and finite volume methods. To obtain high quality meshes, we use Gmsh since it provides refinement and/or optimization options.

Each obtained mesh has a different quality, as calculated using the following metrics:
* `ETA = volume^(2/3)/sum_edge_length^(2)`
* `GAMMA = inscribed_radius/circumscribed_radius`
* `RHO = min_edge_length/max_edge_length`

| TETMSH     	| OPTIM   	| ETA    	| GAMMA  	| RHO    	|
|------------	|---------	|--------	|--------	|--------	|
| DLNY       	| coupled 	| 0.8577 	| 0.7280 	| 0.6572 	|
| FRNTL-DLNY 	| coupled 	| 0.7641 	| 0.6202 	| 0.55   	|
| FRNTL      	| coupled 	| 0.8305 	| 0.6948 	| 0.6168 	|
| MMG3D      	| coupled 	| 0.8491 	| 0.7129 	| 0.635  	|
| DLNY       	| netgen  	| 0.8507 	| 0.7191 	| 0.6459 	|
| FRNTL-DLNY 	| netgen  	| 0.6884 	| 0.55   	| 0.4948 	|
| FRNTL      	| netgen  	| 0.821  	| 0.6846 	| 0.6069 	|
| MMG3D      	| netgen  	| 0.8451 	| 0.7081 	| 0.63   	|
| DLNY       	| gmsh    	| 0.8189 	| 0.6837 	| 0.616  	|
| FRNTL-DLNY 	| gmsh    	| 0.5361 	| 0.4193 	| 0.4029 	|
| FRNTL      	| gmsh    	| 0.758  	| 0.6203 	| 0.5424 	|
| MMG3D      	| gmsh    	| 0.7545 	| 0.6171 	| 0.5391 	|


| METRIC 	| MEAN   	| VAR    	|
|--------	|--------	|--------	|
| ETA    	| 0.5781 	| 0.0056 	|
| GAMMA  	| 0.6465 	| 0.0080 	|
| RHO    	| 0.7811 	| 0.0086 	|


## Optimization schemes (OPTIM)
We employ three optimization schemes: netgen, gmsh, coupled.
The coupled comprises both the netgen and gmsh optimizations.

## Partial target surfaces
Two different bisections are investigated: (1). the surface of the _in silico_ liver was first bisected in the xy, xz, and yz planes, respectively. (2). bisect the three results of (1) along the normal to each of the aforementioned planes obtaining 3 hemi-surfaces.  

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
Both start-up procedures are available as shell scripts from the aforementioned Github repository, e.g. `$ ./ run_msml_sofa . sh`.
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

