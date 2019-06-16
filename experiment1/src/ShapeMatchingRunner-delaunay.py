import os
import msml.api.simulation_runner as api
import msml.ext.misc
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# define charge
charge="10"

# define pathes and files
#msml_outdir= os.path.abspath("/tmp/MSMLResultsLiverShapeMatching_charge"+charge+"/")
msml_outdir= os.path.abspath("/tmp/reg-delaunay_p0.4_ym1000_dt1_t50_c"+charge+"/")
msml_file = os.path.abspath("LiverShapeMatching-delaunay.msml.xml")

msml_mesh = os.path.abspath("delaunay-volume.vtk")
msml_mesh_shape = os.path.abspath("deformed-surface.stl") # for shape matching
#msml_mesh_shape_reference = os.path.abspath("deformed-volume.vtk") # for compare meshes

# run simulation
myRunner = api.SimulationRunner(msml_file, "sofa", msml_outdir)
myRunner.update_variable('vol_mesh', msml_mesh)
myRunner.update_variable('msml_mesh_shape', msml_mesh_shape)
#myRunner.update_variable('msml_mesh_shape_ref', msml_mesh_shape_reference)
myRunner.update_variable('chargeNum', charge)
myRunner.run()
