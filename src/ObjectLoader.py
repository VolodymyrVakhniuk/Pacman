# sefl.objLoader = ObjectLoader( VERTEX_COORDINATES | VERTEX_COLORS | TEXTURE_COORDINATES | VERTEX_NORMAL, INDICES)
# sefl.objLoader = ObjectLoader( VERTEX_COORDINATES | VERTEX_COLORS | TEXTURE_COORDINATES | VERTEX_NORMAL, NO_INDICES)


##########################################
#    # structure of .obj file:           #
#                                        #
#    # mtllib filename.mtl               #
#    # v 1.0 0.1 1.0                     #
#    # v ...                             #
#    # v ...                             #
#                                        #
#    # vt 1.0 0.0                        #
#    # vt ...                            #
#    # vt ...                            #
#                                        #
#    # vn 1.0 0.2 0.8                    #
#    # vn ...                            #
#    # vn ...                            #
#                                        #
#    # usemtl material_1_name            #
#    # f 1/2/3 2/1/1 3/2/1               #
#    # f ...                             #
#    # usemtl material_2_name            #
#    # f ...                             #
#    # f ...                             #
##########################################

from Masks import *

class ObjectLoader:

    def __init__(self, loadDataMask, indicesMask):
        
        self.loadDataMask = loadDataMask

        if loadDataMask & VERTEX_COORDINATES:
            self.vertex_coords_array = []
            self.vertex_coords_vectors = []

        # colors are loader in different way
        if loadDataMask & VERTEX_COLORS == 2:
            self.vertex_colors_array = []

        if loadDataMask & TEXTURE_COORDINATES:
            self.texture_coords_array = []
            self.texture_coords_vectors = []

        if loadDataMask & VERTEX_NORMALS:
            self.vertex_normals_array = []
            self.vertex_normals_vectors = []


        if indicesMask & 0b01:
            self.includeIndices = True
            self.indices = []

        if indicesMask & 0b10:
            self.includeIndices = False




    def loadModel(self, filepath, filename):

        if self.includeIndices == False:
            self.__loadModelNoIndices(filepath, filename)
        else:
            self.__loadModelWithIndices(filepath, filename)
            


    def __loadModelWithIndices(self, filepath, filename):
        
        file = open("../res/models/" + filepath + filename  + ".obj", 'r')

        while True:

            line = file.readline()
            tokens = line.split()

            if line.startswith('mtllib'):
                mtl_filename = "../res/models/" + filepath + tokens[1]

            if self.loadDataMask & 0b0001:
                self.__loadVertexCoordinate(line, tokens)

            if self.loadDataMask & 0b0100:
                self.__loadTextureCoordinate(line, tokens)

            if self.loadDataMask & 0b1000:
                self.__loadVertexNormal(line, tokens)

            if line.startswith('usemtl'):
                break


        # colors are loader in different way
        if self.loadDataMask & VERTEX_COLORS:
            print("COL")
            self.vertex_colors_array = [0] * len(self.vertex_coords_vectors) * 3

        if self.loadDataMask & TEXTURE_COORDINATES:
            print("TEX")
            self.texture_coords_array = [0] * len(self.vertex_coords_vectors) * 3

        if self.loadDataMask & VERTEX_NORMALS:
            print("NOR")
            self.vertex_normals_array = [0] * len(self.vertex_coords_vectors) * 3

        

        while True:
            tokens = line.split()

            if line.startswith('usemtl'):
                material = self.getMaterialFromMtlFile(mtl_filename, tokens[1])
            
            elif line.startswith('f'):
                vertex1_data_str = tokens[1].split('/')
                vertex2_data_str = tokens[2].split('/')
                vertex3_data_str = tokens[3].split('/')


                self.processVertexWithIndices(vertex1_data_str, material)
                self.processVertexWithIndices(vertex2_data_str, material)
                self.processVertexWithIndices(vertex3_data_str, material)

            line = file.readline()

            if not line:
                break


        file.close()

        for vector in self.vertex_coords_vectors:
            self.vertex_coords_array.append(vector[0]) 
            self.vertex_coords_array.append(vector[1]) 
            self.vertex_coords_array.append(vector[2]) 


    def __loadModelNoIndices(self, filepath, filename):
        
        file = open("../res/models/" + filepath + filename  + ".obj", 'r')

        while True:

            line = file.readline()
            tokens = line.split()

            if line.startswith('mtllib'):
                mtl_filename = "../res/models/" + filepath + tokens[1]

            if self.loadDataMask & 0b0001:
                self.__loadVertexCoordinate(line, tokens)

            if self.loadDataMask & 0b0100:
                self.__loadTextureCoordinate(line, tokens)

            if self.loadDataMask & 0b1000:
                self.__loadVertexNormal(line, tokens)

            if line.startswith('usemtl'):
                break


        while True:
            tokens = line.split()

            if line.startswith('usemtl'):
                material = self.getMaterialFromMtlFile(mtl_filename, tokens[1])
            
            elif line.startswith('f'):
                vertex1_data_str = tokens[1].split('/')
                vertex2_data_str = tokens[2].split('/')
                vertex3_data_str = tokens[3].split('/')


                self.processVertexNoIndices(vertex1_data_str, material)
                self.processVertexNoIndices(vertex2_data_str, material)
                self.processVertexNoIndices(vertex3_data_str, material)

            line = file.readline()

            if not line:
                break


        file.close()

        
        
    def __loadVertexCoordinate(self, line, tokens):
        
        if line.startswith('v '):
            self.vertex_coords_vectors.append([
                float(tokens[1]),
                float(tokens[2]),
                float(tokens[3])
            ])


    def __loadTextureCoordinate(self, line, tokens):

        if line.startswith('vt'):
            self.texture_coords_vectors.append([
                float(tokens[1]),
                float(tokens[2])
            ])


    def __loadVertexNormal(self, line, tokens):

        if line.startswith('vn'):
            self.vertex_normals_vectors.append([
                float(tokens[1]),
                float(tokens[2]),
                float(tokens[3])
            ])



    def processVertexNoIndices(self, vertex_data_str, material):
        
        # handle vertex positions
        if self.loadDataMask & VERTEX_COORDINATES:

            vertex_index = int(vertex_data_str[0]) - 1
            vertex_coords_vector = self.vertex_coords_vectors[vertex_index]

            self.vertex_coords_array.append(vertex_coords_vector[0])
            self.vertex_coords_array.append(vertex_coords_vector[1])
            self.vertex_coords_array.append(vertex_coords_vector[2])


        # handle vertex colors
        if self.loadDataMask & VERTEX_COLORS:

            self.vertex_colors_array.append(material[0])
            self.vertex_colors_array.append(material[1])
            self.vertex_colors_array.append(material[2])


        # handle texture coordinates
        if self.loadDataMask & TEXTURE_COORDINATES:

            texture_index = int(vertex_data_str[1]) - 1
            texture_coords_vector = self.texture_coords_vectors[texture_index]

            self.texture_coords_array.append(texture_coords_vector[0])
            self.texture_coords_array.append(texture_coords_vector[1])


        # handle vertex normal
        if self.loadDataMask & VERTEX_NORMALS:
            
            normal_index = int(vertex_data_str[2]) - 1
            normal_vector = self.vertex_normals_vectors[normal_index]

            self.vertex_normals_array.append(normal_vector[0])
            self.vertex_normals_array.append(normal_vector[1])
            self.vertex_normals_array.append(normal_vector[2])



    def processVertexWithIndices(self, vertex_data_str, material):
    
        vertex_index = int(vertex_data_str[0]) - 1
        self.indices.append(vertex_index)

        # handle vertex colors
        if self.loadDataMask & VERTEX_COLORS:
            self.vertex_colors_array[3 * vertex_index + 0] = material[0]
            self.vertex_colors_array[3 * vertex_index + 1] = material[1]
            self.vertex_colors_array[3 * vertex_index + 2] = material[2]



        if self.loadDataMask & TEXTURE_COORDINATES:
            texture_index = int(vertex_data_str[1]) - 1
            texture_vector = self.texture_coords_vectors[texture_index]

            self.texture_coords_array[2 * vertex_index + 0] = texture_vector[0]
            self.texture_coords_array[2 * vertex_index + 1] = texture_vector[1]


        if self.loadDataMask & VERTEX_NORMALS:
            normal_index = int(vertex_data_str[2]) - 1
            normal_vector = self.vertex_normals_vectors[normal_index]

            self.vertex_normals_array[3 * vertex_index + 0] = normal_vector[0]
            self.vertex_normals_array[3 * vertex_index + 1] = normal_vector[1]
            self.vertex_normals_array[3 * vertex_index + 2] = normal_vector[2]


    def getMaterialFromMtlFile(self, mtl_filename, material_name):

        material_found = False
        for line in open(mtl_filename, 'r'):
    
            if line.startswith("newmtl " + material_name):
                material_found = True

            if not material_found:
                continue
            
            if line.startswith('Kd'):
                tokens = line.split()
                return [float(tokens[1]), float(tokens[2]), float(tokens[3])]




########################################
# class ObjectLoader:
#     def __init__(self):
#         self.vertex_coords = []
#         self.vertex_colors = []
#         self.vertex_normals = []
#         self.indices = []


#     def loadModel(self, filepath, filename, includeIndices = True):

#         # lists of 3d vectors
#         vertex_coords_vectors = []
#         vertex_normals_vectors = []

#         file = open("../res/models/" + filepath + filename  + ".obj", 'r')
#         while True:
#             line = file.readline()

#             tokens = line.split()

#             if line.startswith('mtllib'):
#                 mtl_filename = "../res/models/" + filepath + tokens[1]

#             if line.startswith('v '):
#                 vertex_coords_vectors.append([
#                     float(tokens[1]),
#                     float(tokens[2]),
#                     float(tokens[3])
#                 ])

#             if line.startswith('vn'):
#                 vertex_normals_vectors.append([
#                     float(tokens[1]),
#                     float(tokens[2]),
#                     float(tokens[3])
#                 ])

            
#             if line.startswith('usemtl'):
#                 break

        
#         if includeIndices == True:
#             self.vertex_colors = [0] * len(vertex_coords_vectors) * 3
#             self.vertex_normals = [0] * len(vertex_coords_vectors) * 3


#         while True:
#             tokens = line.split()

#             if line.startswith('usemtl'):
#                 material = self.getMaterialFromMtlFile(mtl_filename, tokens[1])
            
#             elif line.startswith('f'):
#                 vertex1_data_str = tokens[1].split('/')
#                 vertex2_data_str = tokens[2].split('/')
#                 vertex3_data_str = tokens[3].split('/')

#                 if includeIndices == True:
#                     self.processVertexWithIndices(vertex1_data_str, vertex_normals_vectors, material)
#                     self.processVertexWithIndices(vertex2_data_str, vertex_normals_vectors, material)
#                     self.processVertexWithIndices(vertex3_data_str, vertex_normals_vectors, material)
#                 else:
#                     self.processVertexNoIndices(vertex1_data_str, vertex_coords_vectors, vertex_normals_vectors, material)
#                     self.processVertexNoIndices(vertex2_data_str, vertex_coords_vectors, vertex_normals_vectors, material)
#                     self.processVertexNoIndices(vertex3_data_str, vertex_coords_vectors, vertex_normals_vectors, material)

#             line = file.readline()

#             if not line:
#                 break


#         file.close()
            
#         if includeIndices == True:
#             for vector in vertex_coords_vectors:
#                 self.vertex_coords.append(vector[0]) 
#                 self.vertex_coords.append(vector[1]) 
#                 self.vertex_coords.append(vector[2]) 


#     def invertNormals(self):
        
#         for i in range(len(self.vertex_normals)):
#             self.vertex_normals[i] = -self.vertex_normals[i]


#     def processVertexWithIndices(self, vertex_data_str, vertex_normals_vectors, material):
        
#         vertex_index = int(vertex_data_str[0]) - 1
#         self.indices.append(vertex_index)

#         self.vertex_colors[3 * vertex_index + 0] = material[0]
#         self.vertex_colors[3 * vertex_index + 1] = material[1]
#         self.vertex_colors[3 * vertex_index + 2] = material[2]

#         normal_index = int(vertex_data_str[2]) - 1
#         normal_vector = vertex_normals_vectors[normal_index]

#         self.vertex_normals[3 * vertex_index + 0] += normal_vector[0]
#         self.vertex_normals[3 * vertex_index + 1] += normal_vector[1]
#         self.vertex_normals[3 * vertex_index + 2] += normal_vector[2]


#     def processVertexNoIndices(self, vertex_data_str, vertex_coords_vectors, vertex_normals_vectors, material):

#         # handle vertex positions
#         vertex_index = int(vertex_data_str[0]) - 1
#         vertex_coords_vector = vertex_coords_vectors[vertex_index]

#         self.vertex_coords.append(vertex_coords_vector[0])
#         self.vertex_coords.append(vertex_coords_vector[1])
#         self.vertex_coords.append(vertex_coords_vector[2])

#         # handle vertex colors
#         self.vertex_colors.append(material[0])
#         self.vertex_colors.append(material[1])
#         self.vertex_colors.append(material[2])

#         # handle vertex normal
#         normal_index = int(vertex_data_str[2]) - 1
#         normal_vector = vertex_normals_vectors[normal_index]

#         self.vertex_normals.append(normal_vector[0])
#         self.vertex_normals.append(normal_vector[1])
#         self.vertex_normals.append(normal_vector[2])


#     def getMaterialFromMtlFile(self, mtl_filename, material_name):

#         material_found = False
#         for line in open(mtl_filename, 'r'):
    
#             if line.startswith("newmtl " + material_name):
#                 material_found = True

#             if not material_found:
#                 continue
            
#             if line.startswith('Kd'):
#                 tokens = line.split()
#                 return [float(tokens[1]), float(tokens[2]), float(tokens[3])]
