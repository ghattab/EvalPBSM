import bpy, bmesh
from bpy import context as C
from mathutils import Vector

def newobj(bm, name):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    ob = bpy.data.objects.new(name,me)
    C.scene.objects.link(ob)
    return ob



# https://blender.stackexchange.com/questions/32283/what-are-all-values-in-bound-box
def bounds(obj, local=False):
    local_coords = obj.bound_box[:]
    om = obj.matrix_world
    if not local:    
        worldify = lambda p: om * Vector(p[:]) 
        coords = [worldify(p).to_tuple() for p in local_coords]
    else:
        coords = [p[:] for p in local_coords]
    rotated = zip(*coords[::-1])
    push_axis = []
    for (axis, _list) in zip('xyz', rotated):
        info = lambda: None
        info.max = max(_list)
        info.min = min(_list)
        info.distance = info.max - info.min
        push_axis.append(info)
    import collections
    originals = dict(zip(['x', 'y', 'z'], push_axis))
    o_details = collections.namedtuple('object_details', 'x y z')
    return o_details(**originals)




object_details = bounds(C.object, True)
bpy.ops.object.mode_set(mode='OBJECT')

cut_index = 0
step_size = 5

bisection_outer = bmesh.new()
bisection_outer.from_mesh(C.object.data)

# split the model into parts along y-axis, with steps of step_size in local coordinate space (this ignores the scale property, so make sure to apply it before)
for i in range(int(round(object_details.y.min)), int(round(object_details.y.max+step_size)), step_size):
        bisection_inner = bisection_outer.copy()
        bmesh.ops.bisect_plane(bisection_outer, geom=bisection_outer.verts[:]+bisection_outer.edges[:]+bisection_outer.faces[:], plane_co=(0,i,0), plane_no=(0,1,0), clear_inner=False)
        bmesh.ops.bisect_plane(bisection_inner, geom=bisection_inner.verts[:]+bisection_inner.edges[:]+bisection_inner.faces[:], plane_co=(0,i,0), plane_no=(0,1,0), clear_outer=True)
        newobj(bisection_inner, "bisect-"+str(cut_index))
        bisection_inner.free()  # free and prevent further access
        cut_index+=1



bisection_outer.free()  # free and prevent further access
bpy.data.objects.remove(C.object, True)
