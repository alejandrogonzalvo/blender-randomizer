import bpy
from random import randrange

intensity = 0.01

for vertice in bpy.context.selected_objects[0].data.vertices:
    vertice.co = [vertice.co[0] + intensity*randrange(-5, 5, 1),
        vertice.co[1] + intensity*randrange(-5, 5, 1),
            vertice.co[2] + intensity*randrange(-5, 5, 1)]
    