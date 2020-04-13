from OpenGL.GL import *

from Shaders.Shader import Shader
import numpy

class LightedObjectShader(Shader):

    def __init__(self):
        super().__init__("LightedObjectVertex", "LightedObjectFragment")

        self.MAX_LIGHTS_NUMBER = 10 
        self.pointLights = []


    # position and color are lists
    def addPointLight(self, position, color):

        if len(self.pointLights) == 10:
            print("CAN NOT ADD MORE POINT LIGHTS")
            return

        self.pointLights.append([position, color])



    def pushPointLights(self):
        
        index = 0
        for light in self.pointLights:

            light_position = light[0]
            light_color = light[1]

            light_position_array = numpy.array(light_position, dtype = numpy.float32)
            light_color_array = numpy.array(light_color, dtype = numpy.float32)

            light_position_uniform_location = self.getUniformLocation("light_positions[" + str(index) + "]")
            light_color_uniform_location = self.getUniformLocation("light_colors[" + str(index) + "]")

            glUniform3fv(light_position_uniform_location, 1, light_position_array)
            glUniform3fv(light_color_uniform_location, 1, light_color_array)

            index += 1


    def setAlphaValue(self, alpha):
        self.setFloat(alpha, "alpha_value")
