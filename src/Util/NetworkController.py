from Util.Network import Network
from queue import Queue

from Actors.ActorsController import ActorsController
from Actors.Direction import Direction


class NetworkController:

    def __init__(self, actorsController : ActorsController):

        self.messageQueue  = Network().getMessageQueue()

        self.actorsController = actorsController


    # Returns True if connected successfully 
    # Returns False if connection is not established / lost
    def checkConnectionToServer(self) -> bool:

        if not Network().isConnected():
            return False
        
        return True


    # Must be called before other functions
    # Returns whether the initialization successful
    def processInitializationData(self) -> bool:
        
        if self.messageQueue.empty():
            return False

        InitString = self.messageQueue.get()

        initializations = InitString.split('\\')

        for initialization in initializations:

            if initialization == 'fin init':
                print("finish initializing")
                return True

            tokens = initialization.split(',')

            actor_kind = tokens[0]
            id = tokens[1]
            spawnX = int(tokens[2])
            spawnY = int(tokens[3])
            speed = float(tokens[4])
            direction = tokens[5]

            if direction == 'a':
                rotationValue = Direction.LEFT
            elif direction == 'w':
                rotationValue = Direction.UP
            elif direction == 'd':
                rotationValue = Direction.RIGHT
            elif direction == 's':
                rotationValue = Direction.DOWN    

            if actor_kind == 'm':
                self.actorsController.initializePlayer1([spawnX, spawnY], rotationValue, speed, id)
            elif actor_kind == 'p':
                self.actorsController.initializePlayer2([spawnX, spawnY], rotationValue, speed, id)
            elif actor_kind == 'g':
                self.actorsController.addGhost([spawnX, spawnY], rotationValue, speed, id)



    def processGameStateData(self) -> False:

        if self.messageQueue.empty():
            return False
        
        data = self.messageQueue.get()

        tokens = data.split(',')
        if tokens[0] == 'turn':

            id = tokens[1]
            self.actorsController.notifyActor(tokens[0] + "/" + tokens[2], id)


    