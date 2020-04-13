from OpenGL.GL import *
from Shaders.TransparentShader import TransparentShader
from Masks import *
from ObjectLoader import ObjectLoader
from Model import Model

from Camera import Camera
from Actors.Pacman import Pacman

import pyrr
import math


class PacmanCore:
    def __init__(self):
    
        self.shader = TransparentShader()
        self.loadModels()

        # list of all pacmans
        self.pacmans = []


    def addPacman(self, pacman : Pacman):
        self.pacmans.append(pacman)


    def loadModels(self):

        # load lower jaw
        pacmanLoader = ObjectLoader(VERTEX_COORDINATES | VERTEX_COLORS, INDICES)
        pacmanLoader.loadModel("pacmanModel/lowerJaw/", "lowerJaw")

        self.lowerJawModel = Model()
        
        self.lowerJawModel.pushData(
            self.shader,
            VERTEX_COORDINATES = pacmanLoader.vertex_coords_array,
            VERTEX_COLORS = pacmanLoader.vertex_colors_array,
            INDICES = pacmanLoader.indices
        )

        # load upper jaw
        pacmanLoader = ObjectLoader(VERTEX_COORDINATES | VERTEX_COLORS, INDICES)
        pacmanLoader.loadModel("pacmanModel/upperJaw/", "upperJaw")

        self.upperJawModel = Model()
        
        self.upperJawModel.pushData(
            self.shader,
            VERTEX_COORDINATES = pacmanLoader.vertex_coords_array,
            VERTEX_COLORS = pacmanLoader.vertex_colors_array,
            INDICES = pacmanLoader.indices
        )


    def render(self, camera : Camera):
    
        self.shader.bind()
        
        self.shader.setViewMatrix(camera.get_view_matrix())
        self.shader.setProjectionMatrix(camera.get_projection_matrix())

        self.shader.setAlphaValue(1.0)

        for pacman in self.pacmans:
            pacman.update()

            lowerJawModelMatrix, upperJawModelMatrix = self.__getLowerThenUpperJawModelMatrix(pacman)

            self.lowerJawModel.bindVAO()
            self.shader.setModelMatrix(lowerJawModelMatrix)
            glDrawElements(GL_TRIANGLES, self.lowerJawModel.indicesCount, GL_UNSIGNED_INT, None)

            self.upperJawModel.bindVAO()
            self.shader.setModelMatrix(upperJawModelMatrix)
            glDrawElements(GL_TRIANGLES, self.upperJawModel.indicesCount, GL_UNSIGNED_INT, None)
        

    def __getLowerThenUpperJawModelMatrix(self, pacman : Pacman):
        
        lowerJawRotation, upperJawRotation = pacman.getLowerThenUpperJawRotations()

        rot_x_lower = pyrr.Matrix44.from_x_rotation(math.radians(lowerJawRotation))
        rot_x_upper = pyrr.Matrix44.from_x_rotation(math.radians(upperJawRotation))

        rot_pacman = pyrr.Matrix44.from_y_rotation(math.radians(pacman.rotation[1]))

        return (
            pyrr.Matrix44.from_translation(pyrr.Vector3(pacman.position)) * rot_pacman * rot_x_lower,
            pyrr.Matrix44.from_translation(pyrr.Vector3(pacman.position)) * rot_pacman * rot_x_upper
        )
