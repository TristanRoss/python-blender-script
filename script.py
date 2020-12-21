import bpy
from math import radians
from random import randint
import time

for obj in bpy.context.scene.objects:
    if obj.type == "MESH" or obj.type == "LIGHT":
        obj.select_set(True)
    else:
        obj.select_set(False)
        
bpy.ops.object.delete()

bpy.context.scene.view_settings.look = 'High Contrast'


camera = bpy.context.scene.camera
for i in range(len(camera.location)):
    camera.location[i] = 0

bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 0

bpy.context.scene.render.resolution_x = 3840
bpy.context.scene.render.resolution_y = 2160


camera.rotation_euler[2] = 0
camera.rotation_euler[1] = 0
camera.rotation_euler[0] = radians(90)

camera.location[1] = -750

for material in bpy.data.materials:
    material.user_clear()
    bpy.data.materials.remove(material)

material = bpy.data.materials.get("Material")
material = bpy.data.materials.new(name="Material")
material.use_nodes = True
material.node_tree.nodes["Principled BSDF"].inputs[17].default_value = (0.1, 0.2, 1, 1)
material.node_tree.nodes["Principled BSDF"].inputs[18].default_value = 5



for i in range(240):
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.active_object
    cube.data.materials.append(material)
    
    random1 = randint(-100, 100)
    random2 = randint(-100, 100)
    random3 = randint(-100, 100)
    random4 = randint(-100, 100)
    random5 = randint(-100, 100)
    random6 = randint(-100, 100)
    random_scale1 = randint(1, 10)
    random_scale2 = randint(1, 10)
    random_scale3 = randint(1, 10)
    cube.location[0] = random1
    cube.location[1] = random2
    cube.location[2] = random3
    cube.scale[0] = random_scale1
    cube.scale[1] = random_scale2
    cube.scale[2] = random_scale3
    cube.animation_data_clear()
    cube.keyframe_insert(data_path="location", frame = 1)
    cube.location[0] += random4
    cube.location[1] += random5
    cube.location[2] += random6
    cube.keyframe_insert(data_path="location", frame = 240)
    cube.animation_data.action.fcurves[0].keyframe_points[0].interpolation = "LINEAR"
    cube.animation_data.action.fcurves[1].keyframe_points[1].interpolation = "LINEAR"
   
bpy.data.cameras["Camera"].clip_end = 1000
camera.animation_data_clear()
camera.keyframe_insert(data_path="location", frame = 1)
camera.location[1] = -600
camera.keyframe_insert(data_path="location", frame = 240)
camera.animation_data.action.fcurves[0].keyframe_points[0].interpolation = "LINEAR"
camera.animation_data.action.fcurves[1].keyframe_points[1].interpolation = "LINEAR"