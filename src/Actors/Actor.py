from Actors.Entity import Entity
from Actors.Maze import Maze

from Actors.Direction import Direction

import pyrr
import math
import numbers
import numpy


class Actor(Entity):

    # position are cell coordinates
    def __init__(self, position : list, direction : Direction, speed : float, id : str):
        super().__init__(Maze.cellCoordsToWorldCoords(position), self.__getRotationVector(direction))

        self.id = id
        self.currectDirection = direction
        self.turnSignal = None
        self.frontVector = self.__getFrontVector(self.currectDirection)
        self.speed = speed / 1000.0
    
    
    def setTurnSignal(self, direction : Direction):
        self.turnSignal = direction


    def canApplyTurnSignal(self, maze : Maze):
        
        currentCellPos = Maze.worldCoordsToCellCoords(self.position)

        return (
            maze.isVacantSpotInSpecifiedDirection(currentCellPos, self.turnSignal) and 
            Maze.isTheMiddleOfTheCell(self.position, self.currectDirection)
        )


    def applyTurnSignal(self):
        
        if self.turnSignal == Direction.LEFT:
            self.position[2] = int(self.position[2]) + numpy.sign(self.position[2]) * 0.5
            self.turnSignal = Direction.NONE
            self.__turnLeft()
        elif self.turnSignal == Direction.UP:
            self.position[0] = int(self.position[0]) + numpy.sign(self.position[0]) * 0.5
            self.turnSignal = Direction.NONE
            self.__turnUp()
        elif self.turnSignal == Direction.RIGHT:
            self.position[2] = int(self.position[2]) + numpy.sign(self.position[2]) * 0.5
            self.turnSignal = Direction.NONE
            self.__turnRight()
        elif self.turnSignal == Direction.DOWN:
            self.position[0] = int(self.position[0]) + numpy.sign(self.position[0]) * 0.5
            self.turnSignal = Direction.NONE
            self.__turnDown()
        

    def __turnLeft(self):
        self.currectDirection = Direction.LEFT
        self.rotation = self.__getRotationVector(Direction.LEFT)
        self.frontVector = self.__getFrontVector(Direction.LEFT)
        

    def __turnUp(self):
        self.currectDirection = Direction.UP
        self.rotation = self.__getRotationVector(Direction.UP)
        self.frontVector = self.__getFrontVector(Direction.UP)
        

    def __turnRight(self):
        self.currectDirection = Direction.RIGHT
        self.rotation = self.__getRotationVector(Direction.RIGHT)
        self.frontVector = self.__getFrontVector(Direction.RIGHT)
        

    def __turnDown(self):
        self.currectDirection = Direction.DOWN
        self.rotation = self.__getRotationVector(Direction.DOWN)
        self.frontVector = self.__getFrontVector(Direction.DOWN)


    def __getRotationVector(self, rotationValue):

        if rotationValue == Direction.NONE:
            rotation = [0.0, 180.0, 0.0]
        
        if rotationValue == Direction.LEFT:
            rotation = [0.0, -90.0, 0.0]

        if rotationValue == Direction.UP:
            rotation = [0.0, 0.0, 0.0]

        if rotationValue == Direction.RIGHT:
            rotation = [0.0, 90.0, 0.0]

        if rotationValue == Direction.DOWN:
            rotation = [0.0, 180.0, 0.0]

        return rotation


    def __getFrontVector(self, rotationValue):

        if rotationValue == Direction.NONE:
            front = [0.0, 0.0, 0.0]
        
        if rotationValue == Direction.LEFT:
            front = [-1.0, 0.0, 0.0]

        if rotationValue == Direction.UP:
            front = [0.0, 0.0, -1.0]

        if rotationValue == Direction.RIGHT:
            front = [1.0, 0.0, 0.0]

        if rotationValue == Direction.DOWN:
            front = [0.0, 0.0, 1.0]

        return front
        