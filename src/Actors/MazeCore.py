from OpenGL.GL import *
from Masks import *
from ObjectLoader import ObjectLoader
from Model import Model
from Shaders.TransparentShader import TransparentShader
import pyrr



class MazeCore:
    def __init__(self):
    
        self.transparentShader = TransparentShader()
        self.loadModels()
        
        self.alpha = 0.5


    def loadModels(self):

        mazeLoader = ObjectLoader(VERTEX_COORDINATES | VERTEX_COLORS, INDICES)
        mazeLoader.loadModel("maze/", "fmaze")

        self.mazeModel = Model()

        self.mazeModel.pushData(
            self.transparentShader,
            VERTEX_COORDINATES = mazeLoader.vertex_coords_array,
            VERTEX_COLORS = mazeLoader.vertex_colors_array,
            INDICES = mazeLoader.indices
        )


    def render(self, camera):

        self.transparentShader.bind()

        self.mazeModel.bindVAO()

        self.transparentShader.setModelMatrix(pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0])))
        self.transparentShader.setViewMatrix(camera.get_view_matrix())
        self.transparentShader.setProjectionMatrix(camera.get_projection_matrix())

        self.transparentShader.setAlphaValue(self.alpha)

        glDepthMask(GL_FALSE);  

        glEnable(GL_CULL_FACE)
        glCullFace(GL_FRONT)
        
        glDrawElements(GL_TRIANGLES, self.mazeModel.indicesCount, GL_UNSIGNED_INT, None)

        glCullFace(GL_BACK)

        glDrawElements(GL_TRIANGLES, self.mazeModel.indicesCount, GL_UNSIGNED_INT, None)
        
        glDisable(GL_CULL_FACE)
        glDepthMask(GL_TRUE)


    # this.maze = [
    #         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    #         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    #         [1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
    #         [1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
    #         [1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1],
    #         [1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1],
    #         [1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1],
    #         [1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1],
    #         [1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1],
    #         [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
    #         [1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1],
    #         [1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1],
    #         [1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
    #         [1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1],
    #         [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
    #         [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
    #         [1,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1],
    #         [1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1],
    #         [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
    #         [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
    #         [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    #         [1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
    #         [1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
    #         [1,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1],
    #         [1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1],
    #         [1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1],
    #         [1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1],
    #         [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
    #         [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
    #         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    #         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #     ];
