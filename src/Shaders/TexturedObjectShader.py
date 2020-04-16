from Shaders.Shader import Shader

class TexturedObjectShader(Shader):

    def __init__(self):
        super().__init__("TexturedObjectVertex", "TexturedObjectFragment")

    