# Non rigid registration
This repository contains results from using the physics-based shape matching or PBSM algorithm on ground truth _in silico_ and _in vitro_ liver models, respectively.

To find out what has the greatest impact on performance, we investigated deformation results using a combination of scenarios: four different tetrahedral meshing algorithms (TETMSH), three different optimization schemes (OPTIM), and six partial target surfaces (bisected from a full Delaunay triangulation). 

## Data
Based on previously published and ground-truth data, we employ the first liver from the _in silico_ validation data and the liver from the phantom experimental data. Suwelack S, Röhl S, Bodenstedt S, Reichard D, Dillmann R, Santos T, Maier‐Hein L, Wagner M, Wünscher J, Kenngott H, Müller BP. Physics‐based shape matching for intraoperative image guidance. Medical physics. 2014 Nov 1;41(11). [Data](http://opencas.webarchiv.kit.edu/?q=PhysicsBasedShapeMatching "Download link") from the Open-CAS: Validating and Benchmarking Computer Assisted Surgery.

## Tetrahedral meshing (TETMSH)
For the scope of this work, we used four TETMSH algorithms: the Delaunay triangulation (DLNY), the Frontal algorithm (FRNTL), the coupled Frontal Delaunay algorithm (FRNTL-DLNY), and the implicit domain mesher (MMG3D). Most of them rely on Tetgen and Netgen algorithms; although both algorithms are characterized as being unstructured algorithms, the created volumes are comparable and are suitable for finite element or FE and finite volume methods. To obtain high quality meshes, we use Gmsh since it provides refinement and/or optimization options.

Each obtained mesh has a different quality, as calculated using the following metrics:
* ETA = volume^(2/3)/sum_edge_length^(2)
* GAMMA = inscribed_radius/circumscribed_radius
* RHO = min_edge_length/max_edge_length

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

## Optimization schemes (OPTIM)

## 
