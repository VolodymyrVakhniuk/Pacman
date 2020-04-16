from OpenGL.GL import *
from Masks import *
from ObjectLoader import ObjectLoader
from Model import Model
from Shaders.ColoredObjectShader import ColoredObjectShader
import pyrr


class MazeCore:
    def __init__(self, shader : ColoredObjectShader):
    
        # self.transparentShader = TransparentShader()
        # self.shader = ColoredObjectShader()
        self.loadModels(shader)
        
        self.modelMatrix = self.__getModelMatrix([0, 0, 0])
        self.alpha_value = 0.5


    def loadModels(self, shader : ColoredObjectShader):

        mazeLoader = ObjectLoader(VERTEX_COORDINATES | VERTEX_COLORS, INDICES)
        mazeLoader.loadModel("maze/", "fmaze")

        self.mazeModel = Model()

        self.mazeModel.pushData(
            shader,
            VERTEX_COORDINATES = mazeLoader.vertex_coords_array,
            VERTEX_COLORS = mazeLoader.vertex_colors_array,
            INDICES = mazeLoader.indices
        )


    # Assume shader is binded
    def render(self, camera, shader : ColoredObjectShader):

        # self.transparentShader.bind()

        # shader.bind()

        self.mazeModel.bindVAO()

        shader.setModelMatrix(self.modelMatrix)
        shader.setViewMatrix(camera.get_view_matrix())
        shader.setProjectionMatrix(camera.get_projection_matrix())
        
        shader.setAlphaValue(self.alpha_value)

        glDepthMask(GL_FALSE);  

        glEnable(GL_CULL_FACE)
        glCullFace(GL_FRONT)
        
        glDrawElements(GL_TRIANGLES, self.mazeModel.indicesCount, GL_UNSIGNED_INT, None)

        glCullFace(GL_BACK)

        glDrawElements(GL_TRIANGLES, self.mazeModel.indicesCount, GL_UNSIGNED_INT, None)
        
        glDisable(GL_CULL_FACE)
        glDepthMask(GL_TRUE)


    def __getModelMatrix(self, position):
        return pyrr.matrix44.create_from_translation(pyrr.Vector3(position))
        

        
