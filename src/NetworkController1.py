from Network1 import Network
from queue import Queue
from GameActors import GameActors
from Actors.Actor import Actor
from Actors.Pacman import Pacman


class NetworkController1:

    def __init__(self, actors : GameActors):

        self.messageQueue  = Network().getMessageQueue()
        #self.connectionQueue = Network().getConnectionQueue()
        self.actors = actors


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
                rotationValue = Actor.Direction.LEFT
            elif direction == 'w':
                rotationValue = Actor.Direction.UP
            elif direction == 'd':
                rotationValue = Actor.Direction.RIGHT
            elif direction == 's':
                rotationValue = Actor.Direction.DOWN    

            if actor_kind == 'm':
                self.actors.player_1_pacman = Pacman([spawnX, spawnY], rotationValue, speed, id)
            elif actor_kind == 'p':
                self.actors.player_2_pacman = Pacman([spawnX, spawnY], rotationValue, speed, id)
            # elif actor_kind == 'g':
            #     self.gameController.addGhost([spawnX, spawnY], rotationValue, speed, id)



    def processGameStateDataData(self) -> False:

        if self.messageQueue.empty():
            return False
        
        data = self.messageQueue.get()
        print(data)

        tokens = data.split(',')

        if tokens[0] == 'turn':
            direction = tokens[2]

            if direction == 'a':
                rotationValue = Actor.Direction.LEFT
            elif direction == 'w':
                rotationValue = Actor.Direction.UP
            elif direction == 'd':
                rotationValue = Actor.Direction.RIGHT
            elif direction == 's':
                rotationValue = Actor.Direction.DOWN    

            print()
            self.actors.player_1_pacman.setTurnSignal(rotationValue)



        

    