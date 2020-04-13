from Actors.Actor import Actor
from Util.Timer import Timer
import pyrr
import math

class Pacman(Actor):
    
    # assume position is 2d vector (x cell, z cell)
    def __init__(self, position : list, rotationValue : Actor.Direction, speed : float, id : str):
        
        super().__init__(position, rotationValue, speed, id)

        self.animation = self.__PacmanAnimation()


    def getLowerThenUpperJawRotations(self):
        return self.animation.getLowerThenUpperJawRotations()
        

    class __PacmanAnimation:

        def __init__(self):
            self.animationPeriod = 1500
            self.amplitude = 60.0

            self.openMouse = True

            self.currentRotationLowerJaw = 0.0
            self.currentRotationUpperJaw = 0.0

            self.timer = Timer()

        
        def getLowerThenUpperJawRotations(self):

            deltaTime = 100 #self.timer.getElapsedTime()
            
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
