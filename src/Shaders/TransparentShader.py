from Shaders.Shader import Shader

class TransparentShader(Shader):
    
    def __init__(self):
        super().__init__("TransparentVertex", "TransparentFragemnt")
        

    def setAlphaValue(self, alpha):
        self.setFloat(alpha, "alpha_value")