from Masks import *
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



# MODEL_VERTEX_COORDINATES = 0
# MODEL_VERTEX_COLORS = 1
# MODEL_VERTEX_NORMALS = 2

# MODEL_INDICES = 3


# class Model:
#     def __init__(self):

#         self.VAO = 0
#         self.VBOcount = 0

#         # for glDrawElements
#         self.indicesCount = 0
#         # for glDrawArrays
#         self.verticesCount = 0

    
#     def addData(self, data, dataType):
        
#         if dataType == MODEL_VERTEX_COORDINATES:
#             self.verticesCount = int(len(data) / 3)

#         data = numpy.array(data, dtype = numpy.float32)

#         if self.VAO == 0:
#             self.VAO = glGenVertexArrays(1)
        
#         glBindVertexArray(self.VAO)


#         if dataType == MODEL_VERTEX_COORDINATES:
#             dimensions = 3
#         elif dataType == MODEL_VERTEX_COLORS:
#             dimensions = 3
#         elif dataType == MODEL_VERTEX_NORMALS:
#             dimensions = 3

#         self.__addVBO(data, dimensions)


#     def addIndices(self, indices):

#         self.indicesCount = len(indices)
#         indices = numpy.array(indices, dtype = numpy.uint32)

#         if self.VAO == 0:
#             self.VAO = glGenVertexArrays(1)

#         glBindVertexArray(self.VAO)

#         self.__addEBO(indices)

    
#     def bindVAO(self):
#         glBindVertexArray(self.VAO)

#     def unbindVAO(self):
#         glBindVertexArray(0)

    
#     def __addVBO(self, data, dimention):

#         VBO = glGenBuffers(1)
#         glBindBuffer(GL_ARRAY_BUFFER, VBO)
#         glBufferData(
#                     GL_ARRAY_BUFFER,
#                     data.size * 4,
#                     data,
#                     GL_STATIC_DRAW
#                     )

#         glVertexAttribPointer(
#                     self.VBOcount,
#                     dimention,
#                     GL_FLOAT,
#                     GL_FALSE,
#                     0,
#                     ctypes.c_void_p(0)
#                     )

#         glEnableVertexAttribArray(self.VBOcount)
#         self.VBOcount += 1


#     def __addEBO(self, indices):

#         EBO = glGenBuffers(1)
#         glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)

#         glBufferData(
#                     GL_ELEMENT_ARRAY_BUFFER,
#                     indices.size * 4,
#                     indices,
#                     GL_STATIC_DRAW
#                     )



# # class Model:
# #     def __init__(self, vertexCoords, vertexColors, normals, indices):

# #         self.vertexCoords = numpy.array(vertexCoords, dtype = numpy.float32)
# #         self.vertexColors = numpy.array(vertexColors, dtype = numpy.float32) 
# #         self.normals = numpy.array(normals, dtype = numpy.float32)

# #         self.indices = numpy.array(indices, dtype = numpy.uint32)

# #         self.indicesCount = len(indices)
# #         self.verticesCount = int(len(vertexCoords) / 3)

# #         self.VBOcount = 0

# #         self.pushData()

    
# #     def addData(self, data):


    
# #     def bindVAO(self):
# #         glBindVertexArray(self.VAO)

# #     def unbindVAO(self):
# #         glBindVertexArray(0)


# #     def pushData(self):

# #         self.VAO = glGenVertexArrays(1)
# #         glBindVertexArray(self.VAO)

# #         self.__addVBO(3, self.vertexCoords)
# #         self.__addVBO(3, self.vertexColors)
# #         self.__addVBO(3, self.normals)
# #         #self.__addEBO()
    
# #     def __addVBO(self, dimention, data):

# #         VBO = glGenBuffers(1)
# #         glBindBuffer(GL_ARRAY_BUFFER, VBO)
# #         glBufferData(
# #                     GL_ARRAY_BUFFER,
# #                     data.size * 4,
# #                     data,
# #                     GL_STATIC_DRAW
# #                     )

# #         glVertexAttribPointer(
# #                     self.VBOcount,
# #                     dimention,
# #                     GL_FLOAT,
# #                     GL_FALSE,
# #                     0,
# #                     ctypes.c_void_p(0)
# #                     )

# #         glEnableVertexAttribArray(self.VBOcount)
# #         self.VBOcount += 1


# #     def __addEBO(self):

# #         EBO = glGenBuffers(1)
# #         glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)

# #         glBufferData(
# #                     GL_ELEMENT_ARRAY_BUFFER,
# #                     self.indices.size * 4,
# #                     self.indices,
# #                     GL_STATIC_DRAW
# #                     )
    


