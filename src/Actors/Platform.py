from OpenGL.GL import *
from Masks import *
from ObjectLoader import ObjectLoader
from Model import Model
from Shaders.BasicShader import BasicShader
from Texture.BasicTexture import BasicTexture
import pyrr


class Platform:
    def __init__(self):

        self.shader = BasicShader()
        self.texture = BasicTexture("maze")

        self.loadModels()


    def loadModels(self):

        # platformLoader = ObjectLoader()
        # platformLoader.loadModel("pacmanModel/lowerJaw/", "lowerJaw", False)

        # self.platformModel = Model()
        # self.platformModel.addData(platformLoader.vertex_coords, VERTEX_COORDINATES)
        # self.platformModel.addData(platformLoader.vertex_colors, VERTEX_COLORS)
        # self.platformModel.addData(platformLoader.vertex_normals, VERTEX_NORMALS)

        platformLoader = ObjectLoader(VERTEX_COORDINATES | TEXTURE_COORDINATES, INDICES)
        platformLoader.loadModel("platform/", "platform")

        self.platformModel = Model()
        self.platformModel.pushData(
            self.shader,
            VERTEX_COORDINATES = platformLoader.vertex_coords_array,
            TEXTURE_COORDINATES = platformLoader.texture_coords_array,
            INDICES = platformLoader.indices
        )


    def render(self, camera):

        self.shader.bind()

        self.shader.setModelMatrix(pyrr.Matrix44.from_translation(pyrr.Vector3([0, -0.01, 0])))
        self.shader.setViewMatrix(camera.get_view_matrix())
        self.shader.setProjectionMatrix(camera.get_projection_matrix())

        self.texture.bind()
        self.platformModel.bindVAO()

        glDrawElements(GL_TRIANGLES, self.platformModel.indicesCount, GL_UNSIGNED_INT, None)
        #glDrawArrays(GL_TRIANGLES, 0, self.platformModel.verticesCount)
        
