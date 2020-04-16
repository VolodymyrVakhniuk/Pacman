from OpenGL.GL import *

from Masks import *
from ObjectLoader import ObjectLoader
from Model import Model

from Shaders.TexturedObjectShader import TexturedObjectShader
from Texture.BasicTexture import BasicTexture

import pyrr


class PlatformCore:
    def __init__(self, shader : TexturedObjectShader):

        # self.shader = BasicShader()
        self.texture = BasicTexture("maze")

        self.loadModels(shader)


    def loadModels(self, shader : TexturedObjectShader):

        platformLoader = ObjectLoader(VERTEX_COORDINATES | TEXTURE_COORDINATES, INDICES)
        platformLoader.loadModel("platform/", "platform")

        self.platformModel = Model()
        self.platformModel.pushData(
            shader,
            VERTEX_COORDINATES = platformLoader.vertex_coords_array,
            TEXTURE_COORDINATES = platformLoader.texture_coords_array,
            INDICES = platformLoader.indices
        )


    # Assume shader is binded
    def render(self, camera, shader : TexturedObjectShader):

        # shader.bind()

        shader.setModelMatrix(pyrr.Matrix44.from_translation(pyrr.Vector3([0, -0.01, 0])))
        shader.setViewMatrix(camera.get_view_matrix())
        shader.setProjectionMatrix(camera.get_projection_matrix())

        self.texture.bind()
        self.platformModel.bindVAO()

        glDrawElements(GL_TRIANGLES, self.platformModel.indicesCount, GL_UNSIGNED_INT, None)
        
