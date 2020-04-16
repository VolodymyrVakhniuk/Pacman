from Actors.Actor import Actor
from Actors.Maze import Maze
from Actors.Direction import Direction
from Util.Timer import Timer
import pyrr
import math
import numpy

class Pacman(Actor):
    
    # assume position is 2d vector (x cell, z cell)
    def __init__(self, position : list, direction : Direction, speed : float, id : str):
        
        super().__init__(position, direction, speed, id)

        self.animation = self.__PacmanAnimation()

        self.updateTimer = Timer()
        self.updateTimer.restart()

        self.isMoving = False


    
    def update(self, maze : Maze):

        deltaTime = self.updateTimer.getElapsedTime()
        distance = deltaTime * self.speed
        self.updateTimer.restart()

        # if self.turnSignal == None:
        #     pass

        if self.canApplyTurnSignal(maze):
            self.applyTurnSignal()
        
        currentCellPos = Maze.worldCoordsToCellCoords(self.position)
        if not maze.isVacantSpotInSpecifiedDirection(currentCellPos, self.currectDirection) and maze.isTheMiddleOfTheCell(self.position, self.currectDirection):
            self.isMoving = False
            return

        self.position += self.frontVector * pyrr.Vector3([distance, distance, distance])
        self.isMoving = True
        



    def notify(self, message : str):
        tokens = message.split('/')

        if tokens[0] == "turn":
            direction = tokens[1]

            if direction[0] == 'a':
                directionValue = Direction.LEFT
            elif direction[0] == 'w':
                directionValue = Direction.UP
            elif direction[0] == 'd':
                directionValue = Direction.RIGHT
            elif direction[0] == 's':
                directionValue = Direction.DOWN
            
            self.setTurnSignal(directionValue)



    def getLowerThenUpperJawRotations(self):
        return self.animation.getLowerThenUpperJawRotations()
        

    class __PacmanAnimation:

        def __init__(self):
            self.animationPeriod = 300
            self.amplitude = 60.0

            self.openMouse = True

            self.currentRotationLowerJaw = 0.0
            self.currentRotationUpperJaw = 0.0

            self.timer = Timer()
            self.timer.restart()

        
        def getLowerThenUpperJawRotations(self):

            deltaTime = self.timer.getElapsedTime()
            
            delta_x_degrees = (deltaTime * self.amplitude) / self.animationPeriod

            if self.currentRotationLowerJaw < 10.0:
                self.openMouse = True
            elif self.currentRotationLowerJaw > self.amplitude:
                self.openMouse = False


            if self.openMouse == True:
                self.currentRotationLowerJaw += delta_x_degrees
            else:
                self.currentRotationLowerJaw -= delta_x_degrees

            self.currentRotationUpperJaw = -self.currentRotationLowerJaw

            self.timer.restart()

            return self.currentRotationLowerJaw, self.currentRotationUpperJaw
