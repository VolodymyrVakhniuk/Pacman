from OpenGL.GL import *
from OpenGL.GL.shaders import *

import pyrr

class Shader:

    def __init__(self, vertexShaderFile, fragmentShaderFile):

        vf = open("../res/shaders/" + vertexShaderFile + ".glsl", "r")
        vertexShaderSource = vf.read()

        ff = open("../res/shaders/" + fragmentShaderFile + ".glsl", "r")
        fragmentShaderSource = ff.read()

        VAO = glGenVertexArrays(1)
        glBindVertexArray(VAO)

        vertexShader = compileShader(vertexShaderSource, GL_VERTEX_SHADER)
        fragmentShader = compileShader(fragmentShaderSource, GL_FRAGMENT_SHADER)

        self.shader = compileProgram(vertexShader, fragmentShader)


    def bind(self):
        glUseProgram(self.shader)


    def unbind(self):
        glUseProgram(0)


    def getUniformLocation(self, uniformName):
        return glGetUniformLocation(self.shader, uniformName)


    def getAttributeLocation(self, uniformName):
        return glGetAttribLocation(self.shader, uniformName)

    
    def setModelMatrix(self, modelMatrix):
        ul = glGetUniformLocation(self.shader, "modelMatrix")
        glUniformMatrix4fv(ul, 1, GL_FALSE, modelMatrix)


    def setViewMatrix(self, viewMatrix):
        ul = glGetUniformLocation(self.shader, "viewMatrix")
        glUniformMatrix4fv(ul, 1, GL_FALSE, viewMatrix)


    def setProjectionMatrix(self, projectionMatrix):
        ul = glGetUniformLocation(self.shader, "projectionMatrix")
        glUniformMatrix4fv(ul, 1, GL_FALSE, projectionMatrix)


    # vector is a pyrr.Vector3
    def setVector3(self, vector, uniformName):
        ul = glGetUniformLocation(self.shader, uniformName)
        glUniform3fv(ul, 1, vector)

    def setFloat(self, val, uniformName):
        ul = glGetUniformLocation(self.shader, uniformName)
        glUniform1fv(ul, 1, val)
