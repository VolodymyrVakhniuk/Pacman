from Shaders.Shader import Shader

class BasicShader(Shader):

    def __init__(self):
        super().__init__("BasicVertex", "BasicFragment")

    