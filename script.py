import bpy
from math import radians
from random import randint
import time

camera = bpy.context.scene.camera
for i in range(len(camera.location)):
    camera.location[i] = 0

camera.rotation_euler[2] = 0
camera.rotation_euler[1] = 0
camera.rotation_euler[0] = radians(90)

camera.location[1] = -3;

for i in range(240):
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.active_object
    
    random1 = randint(-100, 100)
    random2 = randint(-100, 100)
    random3 = randint(-100, 100)
    random_scale = randint(1, 5)
    cube.location[0] = random1
    cube.location[1] = random2
    cube.location[2] = random3
    cube.scale[0] = random_scale
    cube.scale[1] = random_scale
    cube.scale[2] = random_scale
    
