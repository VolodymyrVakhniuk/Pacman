from Shaders.Shader import Shader
import pyrr

class PointLightShader(Shader):

    def __init__(self):
        super().__init__("PointLightVertex", "PointLightFragment")
    
    # color is a list of size 3
    def setLightColor(self, color):
        
       self.setVector3(pyrr.Vector3(color) , "light_color")





