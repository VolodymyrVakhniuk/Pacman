# from GameController import GameController
# from Actors.Pacman import Pacman
# from Actors.Actor import Actor

# from Util.Network import Network
# from enum import Enum

# class NetworkController:

#     class Status(Enum):

#         CONNECTING_TO_SERVER = 0,
#         CONNECTED_TO_SERVER = 1,
#         WAITING_FOR_INITIALIZATION = 2,
#         INITIALIZING_NOW = 3,
#         INITIALIZATION_DONE = 4,

#         PROCESSING_ACTORS_MOVEMENTS = 5
    


#     def __init__(self, gameController : GameController):

#         self.gameController = gameController

#         self.connectedToServer = False
#         self.initializationDone = False

#         #self.status = NetworkController.Status.CONNECTING_TO_SERVER
#         self.network = Network()
#         self.connectedToServer = True
#         #self.status = NetworkController.Status.CONNECTED_TO_SERVER


#     # def processRecievedData(self):
        
#     #     data = self.network.recieveData()

#     #     if self.status == NetworkController.Status.WAITING_FOR_INITIALIZATION:
#     #         self.status = NetworkController.Status.INITIALIZING_NOW
#     #         self.__initializeComponents(data)
#     #     else:
#     #         self.status == NetworkController.Status.PROCESSING_ACTORS_MOVEMENTS
#     #         self.__processGameFlow(data)
                

#     def initializeComponents(self):
        
#         data = self.network.recieveData()
    
#         initializations = data.split('\\')

#         for initialization in initializations:

#             if initialization == 'fin init':
#                 print("finish initializing")
#                 self.initializationDone = True
#                 return

#             tokens = initialization.split(',')

#             actor_kind = tokens[0]
#             id = tokens[1]
#             spawnX = int(tokens[2])
#             spawnY = int(tokens[3])
#             speed = float(tokens[4])
#             direction = tokens[5]

#             if direction == 'a':
#                 rotationValue = Pacman.Direction.LEFT
#             elif direction == 'w':
#                 rotationValue = Pacman.Direction.UP
#             elif direction == 'd':
#                 rotationValue = Pacman.Direction.RIGHT
#             elif direction == 's':
#                 rotationValue = Pacman.Direction.DOWN    

#             if actor_kind == 'm':
#                 self.gameController.player_1_pacman = Pacman([spawnX, spawnY], rotationValue, speed, id)
#             elif actor_kind == 'p':
#                 self.gameController.player_2_pacman = Pacman([spawnX, spawnY], rotationValue, speed, id)
#             elif actor_kind == 'g':
#                 self.gameController.addGhost([spawnX, spawnY], rotationValue, speed, id)



#     def __processGameFlow(self, data : str):

#         tokens = data.split(',')
#         print(tokens)

#         # if len(tokens) != 3:
#         #     return

#         # if tokens[2] == 'a':
#         #     self.gameController.player_1_pacman.turnLeft()
#         # elif tokens[2] == 'w':
#         #     self.gameController.player_1_pacman.turnUp()
#         # elif tokens[2] == 'd':
#         #     self.gameController.player_1_pacman.turnRight()
#         # elif tokens[2] == 's':
#         #     self.gameController.player_1_pacman.turnDown()




#     def getStatus(self):
        
#         return self.Status



# # class NetworkDataParser:

# #     def __init__(self, gameController : GameController):

# #         self.gameController = gameController
# #         self.isInitializationDone = False


# #     def parse(self, data : str):
# #         if not self.isInitializationDone:
# #             self.parsingFunction = self.__parseInitialization

# #         else:
# #             self.parsingFunction = self.__parseGameInput
# #             self.isInitializationDone = True


        

# #         self.parsingFunction(data)


# #     def __parseInitialization(self, data : str):

# #         lines = data.split('\\')

# #         for line in lines:

# #             if line == 'fin init':
# #                 print("finish initializing")
# #                 self.isInitializationDone = True
# #                 return

# #             tokens = line.split(',')

# #             player = tokens[0]
# #             id = tokens[1]
# #             spawnX = int(tokens[2])
# #             spawnY = int(tokens[3])
# #             speed = float(tokens[4])
# #             direction = tokens[5]

# #             if direction == 'a':
# #                 rotationValue = Pacman.Direction.LEFT
# #             elif direction == 'w':
# #                 rotationValue = Pacman.Direction.UP
# #             elif direction == 'd':
# #                 rotationValue = Pacman.Direction.RIGHT
# #             elif direction == 's':
# #                 rotationValue = Pacman.Direction.DOWN    

# #             if player == 'm':
# #                 self.gameController.player_1_pacman = Pacman([spawnX, spawnY], rotationValue, speed, id)
            



# #     def __parseGameInput(self, data : str):
# #         #print("input = " + data)

# #         tokens = data.split(',')
# #         print(tokens)

# #         if len(tokens) != 3:
# #             return

# #         if tokens[2] == 'a':
# #             self.gameController.player_1_pacman.turnLeft()
# #         elif tokens[2] == 'w':
# #             self.gameController.player_1_pacman.turnUp()
# #         elif tokens[2] == 'd':
# #             self.gameController.player_1_pacman.turnRight()
# #         elif tokens[2] == 's':
# #             self.gameController.player_1_pacman.turnDown()




# #     def IsInitializationDone(self):
# #         return self.isInitializationDone

