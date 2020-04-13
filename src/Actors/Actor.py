from enum import Enum
from Util.Timer import Timer

from Actors.Entity import Entity
from Actors.Maze import Maze


import pyrr
import math
import numbers
import numpy

class Actor(Entity):

    class Direction(Enum):
        NONE = -1
        LEFT = 0
        UP = 1
        RIGHT = 2
        DOWN = 3

    
    def __init__(self, position : list, rotationValue : Direction, speed : float, id : str):
        super().__init__(self.__cellCoordsToWorldCoords(position), self.__getRotationVector(rotationValue))

        self.frontVector = self.__getFrontVector(rotationValue)
        
        self.maze = Maze()
    
        # one cell in 1 sec // 1/1000 cells in 1 millisec
        self.speed = speed / 1000.0 #5.0/1000.0

        self.turnSignal = None

        self.timer = Timer()
        self.timer.restart()


    def update(self):
        
        deltaTime = self.timer.getElapsedTime()
        self.timer.restart()
        
        distance = deltaTime * self.speed

        # print(self.position)
        # print(self.__worldCoordsToCellCoords(self.position))

        if self.turnSignal == None:
            pass

        elif self.turnSignal == Actor.Direction.LEFT:
            
            if self.isInTheMiddleOfTheCell():
                cellPos = self.__worldCoordsToCellCoords(self.position)
                if self.maze.maze[cellPos[1]][cellPos[0] - 1] == 0:
                    self.position[2] = int(self.position[2]) + numpy.sign(self.position[2]) * 0.5
                    self.turnSignal = Actor.Direction.NONE
                    self.turnLeft()
        
        elif self.turnSignal == Actor.Direction.UP:
            
            if self.isInTheMiddleOfTheCell():
                cellPos = self.__worldCoordsToCellCoords(self.position)
                if self.maze.maze[cellPos[1] - 1][cellPos[0]] == 0:
                    self.position[0] = int(self.position[0]) + numpy.sign(self.position[0]) * 0.5
                    self.turnSignal = Actor.Direction.NONE
                    self.turnUp()


        elif self.turnSignal == Actor.Direction.RIGHT:
            
            if self.isInTheMiddleOfTheCell():
                cellPos = self.__worldCoordsToCellCoords(self.position)
                if self.maze.maze[cellPos[1]][cellPos[0] + 1] == 0:
                    self.position[2] = int(self.position[2]) + numpy.sign(self.position[2]) * 0.5
                    self .turnSignal = Actor.Direction.NONE
                    self.turnRight()

        elif self.turnSignal == Actor.Direction.DOWN:
            
            if self.isInTheMiddleOfTheCell():
                cellPos = self.__worldCoordsToCellCoords(self.position)
                if self.maze.maze[cellPos[1] + 1][cellPos[0]] == 0:
                    self.position[0] = int(self.position[0]) + numpy.sign(self.position[0]) * 0.5
                    self.turnSignal = Actor.Direction.NONE
                    self.turnDown()
    
        
        cellPos = self.__worldCoordsToCellCoords(self.position)
        if self.maze.maze[cellPos[1] + int(self.frontVector[2])][cellPos[0] + int(self.frontVector[0])] == 1:
            if self.isInTheMiddleOfTheCell():
                return
        

        self.position += self.frontVector * pyrr.Vector3([distance, distance, distance])


    
    def setTurnSignal(self, direction : Direction):
        self.turnSignal = direction



    def turnLeft(self):
        self.pacmanDirection = Actor.Direction.LEFT
        self.rotation = self.__getRotationVector(Actor.Direction.LEFT)
        self.frontVector = self.__getFrontVector(Actor.Direction.LEFT)
        

    def turnUp(self):
        self.pacmanDirection = Actor.Direction.UP
        self.rotation = self.__getRotationVector(Actor.Direction.UP)
        self.frontVector = self.__getFrontVector(Actor.Direction.UP)
        

    def turnRight(self):
        self.pacmanDirection = Actor.Direction.RIGHT
        self.rotation = self.__getRotationVector(Actor.Direction.RIGHT)
        self.frontVector = self.__getFrontVector(Actor.Direction.RIGHT)
        

    def turnDown(self):
        self.pacmanDirection = Actor.Direction.DOWN
        self.rotation = self.__getRotationVector(Actor.Direction.DOWN)
        self.frontVector = self.__getFrontVector(Actor.Direction.DOWN)


    def __cellCoordsToWorldCoords(self, cellCoords):
        
        cellBias = 0.5

        position = [cellCoords[0] - 14 + cellBias, 0.6, cellCoords[1] - 16 + cellBias]
        return position
    

    def __worldCoordsToCellCoords(self, worldCoords):
        
        position = [math.floor(worldCoords[0]) + 14, math.floor(worldCoords[2]) + 16]
        return position

    
    def isInTheMiddleOfTheCell(self):

        truncatedValueX = abs(self.position[0] - int(self.position[0]))
        truncatedValueZ = abs(self.position[2] - int(self.position[2]))

        if  (0.49 < truncatedValueX < 0.51) and (0.49 < truncatedValueZ < 0.51):
            return True

        return False


    def __getRotationVector(self, rotationValue):

        if rotationValue == Actor.Direction.NONE:
            rotation = [0.0, 180.0, 0.0]
        
        if rotationValue == Actor.Direction.LEFT:
            rotation = [0.0, -90.0, 0.0]

        if rotationValue == Actor.Direction.UP:
            rotation = [0.0, 0.0, 0.0]

        if rotationValue == Actor.Direction.RIGHT:
            rotation = [0.0, 90.0, 0.0]

        if rotationValue == Actor.Direction.DOWN:
            rotation = [0.0, 180.0, 0.0]

        return rotation


    def __getFrontVector(self, rotationValue):

        if rotationValue == Actor.Direction.NONE:
            front = [0.0, 0.0, 0.0]
        
        if rotationValue == Actor.Direction.LEFT:
            front = [-1.0, 0.0, 0.0]

        if rotationValue == Actor.Direction.UP:
            front = [0.0, 0.0, -1.0]

        if rotationValue == Actor.Direction.RIGHT:
            front = [1.0, 0.0, 0.0]

        if rotationValue == Actor.Direction.DOWN:
            front = [0.0, 0.0, 1.0]

        return front
        