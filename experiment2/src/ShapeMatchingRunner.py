import os
import msml.api.simulation_runner as api
import msml.ext.misc
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt




# define charge
# test: 1000, 10, 2500, 5000
charge="500"

# define pathes and files
#msml_outdir= os.path.abspath("/tmp/MSMLResultsLiverShapeMatching_charge"+charge+"/")
msml_outdir= os.path.abspath("/tmp/reg-phantom_p0.4_ym1000_dt0.5_t200_c"+charge+"/")
msml_file = os.path.abspath("LiverShapeMatching.msml.xml")

msml_mesh = os.path.abspath("InitialLowResolutionVolumeModel.vtk")
msml_mesh_shape = os.path.abspath("partial-intra-auto2.stl") # for shape matching
#msml_mesh_shape_reference = os.path.abspath("deformed-volume.vtk") # for compare meshes

# run simulation
myRunner = api.SimulationRunner(msml_file, "sofa", msml_outdir)
myRunner.update_variable('vol_mesh', msml_mesh)
myRunner.update_variable('msml_mesh_shape', msml_mesh_shape)
#myRunner.update_variable('msml_mesh_shape_ref', msml_mesh_shape_reference)
myRunner.update_variable('chargeNum', charge)
myRunner.run()

# compare meshes
#errorVec = myRunner.get_results('compMesh', 'errorVec')
#dispVec = myRunner.get_results('compMeshDisp', 'errorVec')

#print "Checking for vector lengths ..."
#print len(errorVec)
#print len(dispVec)

# plotting
#fig1, ax1 = plt.subplots(figsize=(10,6))
#bp1 = plt.boxplot(errorVec)
#ax1.set_ylabel('Error [mm]')
#plt.xticks( [1], ['Deformation Error'] )

#plt.savefig("def.pdf")

#fig2, ax2 = plt.subplots(figsize=(10,6))
#bp2 = plt.boxplot(dispVec)
#ax2.set_ylabel('Error [mm]')
#plt.xticks( [1], ['Displacement'] )

#plt.show()
#plt.savefig("dis.pdf")


#f = open("def.txt", "w+")
#f.write(str(errorVec))
#f.close()

#f = open("dis.txt", "w+")
#f.write(str(dispVec))
#f.close()