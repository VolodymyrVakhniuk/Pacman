from Masks import *
from ObjectLoader import ObjectLoader
from Model import Model

import pyrr

class PointLight:
    def __init__(self, light_position, light_color):
        
        lampLoader = ObjectLoader(VERTEX_COORDINATES | VERTEX_COLORS | VERTEX_NORMALS, NO_INDICES)
        lampLoader.loadModel("lamp/", "lamp")

        self.model = Model()

        self.model.pushData(
            
        )
        
        # lampLoader = ObjectLoader()
        # lampLoader.loadModel("lamp/", "lamp", False)

        # self.model = Model()

        # self.model.addData(lampLoader.vertex_coords, VERTEX_COORDINATES)
        # self.model.addData(lampLoader.vertex_colors, VERTEX_COLORS)
        # self.model.addData(lampLoader.vertex_normals, VERTEX_NORMALS)

        self.position = light_position
        self.color = light_color


    def get_model_matrix(self):
        return pyrr.matrix44.create_from_translation(pyrr.Vector3(self.position))
