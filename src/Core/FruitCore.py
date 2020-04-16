from OpenGL.GL import *
from Masks import *
from ObjectLoader import ObjectLoader
from Model import Model

from Actors.Fruits import Fruits
from Actors.Maze import Maze

from Shaders.InstancingShader import InstancingShader
from Camera import Camera

import pyrr


class FruitCore():

    def __init__(self, shader : InstancingShader, fruits : Fruits):

        self.fruitCount = 0
        self.fruits = fruits

        self.offsetsX = []
        self.offsetsY = []

        self.__setOffsets()

        self.loadModels(shader)

    
    def loadModels(self, shader : InstancingShader):
        
        fruitLoader = ObjectLoader(VERTEX_COORDINATES | VERTEX_COLORS, INDICES)
        fruitLoader.loadModel("fruits/", "fruit")

        self.fruitModel = Model()
        
        self.fruitModel.pushData(
            shader,
            VERTEX_COORDINATES = fruitLoader.vertex_coords_array,
            VERTEX_COLORS = fruitLoader.vertex_colors_array,
            INDICES = fruitLoader.indices
        )


    def update(self):
        
        if self.fruits.fruitPositionsChanged == True:
            print("CHANGED")
            self.__setOffsets()



    # Assume shader is binded
    def render(self, camera : Camera, shader : InstancingShader):

        shader.bind()
        self.fruitModel.bindVAO()

        shader.loadOffsets(self.offsetsX, self.offsetsY)

        shader.setModelMatrix(pyrr.Matrix44.from_translation(pyrr.Vector3([0.0, 0.5, 0.0])))
        shader.setViewMatrix(camera.get_view_matrix())
        shader.setProjectionMatrix(camera.get_projection_matrix())
    
        glDrawElementsInstanced(GL_TRIANGLES, self.fruitModel.indicesCount, GL_UNSIGNED_INT, None, self.fruitCount)



    # for instancing
    def __setOffsets(self):

        self.fruitCount = len(self.fruits.fruitPositions)
        print(self.fruitCount)

        self.offsetsX.clear()
        self.offsetsY.clear()
        
        for position in self.fruits.fruitPositions:
            
            worldPos = Maze.cellCoordsToWorldCoords(position)

            self.offsetsX.append(worldPos[0])
            self.offsetsY.append(worldPos[2])

