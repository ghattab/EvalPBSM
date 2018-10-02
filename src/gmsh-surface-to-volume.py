#!/usr/bin/env python

"""
Create a tetrahedral volume from a surface mesh.
3D meshing converts an .stl file to .vtk file using Gmsh
"""

import os
import sys
import subprocess


if len(sys.argv) < 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("Usage: gmsh-surface-to-volume.py <input.stl> <output.vtk>")
    sys.exit(1)

# write gmsh geofile
geofile = os.path.join("base.geo")
g = open(geofile, "w")
g.write("Mesh.Algorithm3D=5;\n")
# Mesh.Algorithm
# 1=Delaunay, 4=Frontal, 5=Frontal Delaunay, 7=MMG3D
g.write("Mesh.Optimize=1;\n")
g.write("Mesh.OptimizeNetgen=1;\n")
g.write("Merge \"" + sys.argv[1] + "\";\n")
g.write("Surface Loop(1) = {1};\n")
g.write("Volume(1) = {1};\n")
g.write("Physical Volume(1) = {1};\n")
g.close()

#  -order 2 3            Second order elements in 3D (quadratic tetrahedra)
#  -optimize_ho          Optimize high order meshes
#  -ho_[min,max,nlayers] High-order optimization parameters
bashCommand = "gmsh base.geo -o " + sys.argv[2] + " -3 -order 1"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
