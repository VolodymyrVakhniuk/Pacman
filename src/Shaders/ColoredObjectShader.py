from Shaders.Shader import Shader

class ColoredObjectShader(Shader):
    
    def __init__(self):
        super().__init__("ColoredObjectVertex", "ColoredObjectFragment")
        

    def setAlphaValue(self, alpha):
        self.setFloat(alpha, "alpha_value")