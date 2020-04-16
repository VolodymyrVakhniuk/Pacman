from OpenGL.GL import *
from Camera import Camera

from Masks import *
from Model import Model
from ObjectLoader import ObjectLoader

from Shaders.ColoredObjectShader import ColoredObjectShader
from Actors.Ghost import Ghost

import pyrr
import math


class GhostCore:

    def __init__(self, shader : ColoredObjectShader):
        
        self.loadModels(shader)

        self.ghosts = []


    def addGhost(self, ghost : Ghost):
        self.ghosts.append(ghost)


    def loadModels(self, shader : ColoredObjectShader):

        self.redGhostModel = self.__loadGhost(Ghost.GhostColor.RED, shader)
        self.orangeGhostModel = self.__loadGhost(Ghost.GhostColor.ORANGE, shader)
        self.purpleGhostModel = self.__loadGhost(Ghost.GhostColor.PURPLE, shader)
        self.coralGhostModel = self.__loadGhost(Ghost.GhostColor.GREEN, shader)
        

    # Assume shader is binded
    def render(self, camera : Camera, shader : ColoredObjectShader):
        
        shader.setViewMatrix(camera.get_view_matrix())
        shader.setProjectionMatrix(camera.get_projection_matrix())

        shader.setAlphaValue(1.0)

        for ghost in self.ghosts:

            if ghost.ghostColor == Ghost.GhostColor.RED:
                model = self.redGhostModel
            elif ghost.ghostColor == Ghost.GhostColor.ORANGE:
                model = self.orangeGhostModel
            elif ghost.ghostColor == Ghost.GhostColor.PURPLE:
                model = self.purpleGhostModel
            elif ghost.ghostColor == Ghost.GhostColor.GREEN:
                model = self.coralGhostModel

            model.bindVAO()
            shader.setModelMatrix(self.__getModelMatrix(ghost))

            glDrawElements(GL_TRIANGLES, model.indicesCount, GL_UNSIGNED_INT, None)


    def __getModelMatrix(self, ghost : Ghost):

        rot_ghost = pyrr.Matrix44.from_y_rotation(math.radians(ghost.rotation[1]))
        
        return pyrr.Matrix44.from_translation(pyrr.Vector3(ghost.position)) * rot_ghost
            

    def __loadGhost(self, ghostColor : Ghost.GhostColor, shader : ColoredObjectShader):
        
        if ghostColor == Ghost.GhostColor.RED:
            filename = "RedGhost"
        elif ghostColor == Ghost.GhostColor.ORANGE:
            filename = "OrangeGhost"
        elif ghostColor == Ghost.GhostColor.PURPLE:
            filename = "PurpleGhost"
        elif ghostColor == Ghost.GhostColor.GREEN:
            filename = "GreenGhost"

        ghostLoader = ObjectLoader(VERTEX_COORDINATES | VERTEX_COLORS, INDICES)
        ghostLoader.loadModel("ghost/", filename)

        ghostModel = Model()
        
        ghostModel.pushData(
            shader,
            VERTEX_COORDINATES = ghostLoader.vertex_coords_array,
            VERTEX_COLORS = ghostLoader.vertex_colors_array,
            INDICES = ghostLoader.indices
        )

        return ghostModel