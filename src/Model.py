from OpenGL.GL import *
import numpy

class Model:
    
    def __init__(self):
        
        self.VAO = 0

        #for glDrawElements
        self.indicesCount = 0
        #for glDrawArrays
        self.verticesCount = 0
        

    def pushData(self, shader, **kwargs):
        
        self.VAO = glGenVertexArrays(1)
        glBindVertexArray(self.VAO)
    
        for key, data in kwargs.items():
            
            if key == "VERTEX_COORDINATES":
                self.verticesCount = len(data)
                self.__addVBO(numpy.array(data, dtype = numpy.float32), 3, shader.getAttributeLocation("in_position"))

            elif key == "VERTEX_COLORS":
                self.__addVBO(numpy.array(data, dtype = numpy.float32), 3, shader.getAttributeLocation("in_color"))
            
            elif key == "TEXTURE_COORDINATES":
                self.__addVBO(numpy.array(data, dtype = numpy.float32), 2, shader.getAttributeLocation("in_texture_coords"))
            
            elif key == "VERTEX_NORMALS":
                self.__addVBO(numpy.array(data, dtype = numpy.float32), 3, shader.getAttributeLocation("in_normal"))

            elif key == "INDICES":
                self.indicesCount = len(data)
                print("INDICES LEN = " + str(self.indicesCount))
                self.__addEBO(numpy.array(data, dtype = numpy.uint32))


    def bindVAO(self):
        glBindVertexArray(self.VAO)

    def unbindVAO(self):
        glBindVertexArray(0)

    
    def __addVBO(self, data, dimention, attributeLocation):

        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(
                    GL_ARRAY_BUFFER,
                    data.size * 4,
                    data,
                    GL_STATIC_DRAW
                    )

        glVertexAttribPointer(
                    attributeLocation,
                    dimention,
                    GL_FLOAT,
                    GL_FALSE,
                    0,
                    ctypes.c_void_p(0)
                    )

        glEnableVertexAttribArray(attributeLocation)


    def __addEBO(self, indices):

        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)

        glBufferData(
                    GL_ELEMENT_ARRAY_BUFFER,
                    indices.size * 4,
                    indices,
                    GL_STATIC_DRAW
                    )

    


