from OpenGL.GL import *
from Shaders.Shader import Shader

class InstancingShader(Shader):

    def __init__(self):
        super().__init__("InstancingVertex", "InstancingFragment")


    def loadOffsets(self, offsetsX : list, offsetsY : list):
        
        index = 0
        for offsetX in offsetsX:
            # uniform_location = self.getUniformLocation("offsetsX[" + str(index) + "]")
            # # self.setFloat(uniform_location, 1, GL_FALSE, offsetX)
            self.setFloat(offsetX, "offsetsX[" + str(index) + "]")
            index += 1

        index = 0
        for offsetY in offsetsY:
            # uniform_location = self.getUniformLocation("offsetsY[" + str(index) + "]")
            # self.setFloat(uniform_location, 1, GL_FALSE, offsetY)

            self.setFloat(offsetY, "offsetsY[" + str(index) + "]")
            index += 1


    # list of model matrices
    def loadModelMatrices(self, matrices : list):
        
        # uniform_location = self.getUniformLocation("modelMatrices[0]")
        # glUniformMatrix4fv(uniform_location, 1, GL_FALSE, matrices[0])

        # uniform_location = self.getUniformLocation("modelMatrices[1]")
        # glUniformMatrix4fv(uniform_location, 1, GL_FALSE, matrices[1])

        index = 0
        for matrix in matrices:

            uniform_location = self.getUniformLocation("modelMatrices[" + str(index) + "]")
            glUniformMatrix4fv(uniform_location, 1, GL_FALSE, matrix)
            index += 1
