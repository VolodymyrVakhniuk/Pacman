import glfw
from InputHandlers.Command import MoveLeft, MoveUp, MoveRight, MoveDown
from Actors.Pacman import Pacman
from Actors.Direction import Direction

from Util.Network import Network
from Util.Timer import Timer

import threading
import math


class PacmanInputHandler:

    def __init__(self, pacman : Pacman):

        self.pacman = pacman

        self.buttonJ = MoveLeft()
        self.buttonI = MoveUp()
        self.buttonL = MoveRight()
        self.buttonK = MoveDown()

        self.timer = Timer()
        self.timer.restart()

        self.dataToSend = 'n'
        self.previousData = 'n'

        self.alreadySend = False

    
    def handleInput(self, window):
        
            if glfw.get_key(window, glfw.KEY_J) == glfw.PRESS:
                self.dataToSend = 'a'

            if glfw.get_key(window, glfw.KEY_I) == glfw.PRESS:
                self.dataToSend = 'w'

            if glfw.get_key(window, glfw.KEY_L) == glfw.PRESS:
                self.dataToSend = 'd'

            if glfw.get_key(window, glfw.KEY_K) == glfw.PRESS:
                self.dataToSend = 's'

            
            if self.dataToSend == self.previousData:
                return

            if not self.pacman.isMoving and not self.alreadySend:
                if self.dataToSend != 'n' :
                    Network().sendData(self.dataToSend)
                    self.previousData = self.dataToSend
                    self.alreadySend = True

            elif not self.alreadySend:
                if self.pacman.currectDirection == Direction.LEFT:
                    if 0.9 > (self.pacman.position[0] - math.floor(self.pacman.position[0])) > 0.8:
                        print("Sending LEFT " + self.dataToSend)
                        Network().sendData(self.dataToSend)
                        self.previousData = self.dataToSend
                        self.alreadySend = True

                elif self.pacman.currectDirection == Direction.RIGHT:
                    if 0.1 < (self.pacman.position[0] - math.floor(self.pacman.position[0])) < 0.2:
                        print("Sending RIGHT " + self.dataToSend)
                        Network().sendData(self.dataToSend)
                        self.previousData = self.dataToSend
                        self.alreadySend = True
                
                elif self.pacman.currectDirection == Direction.UP:
                    if 0.1 < (self.pacman.position[2] - math.floor(self.pacman.position[2])) < 0.2:
                        print("Sending UP " + self.dataToSend)
                        Network().sendData(self.dataToSend)
                        self.previousData = self.dataToSend
                        self.alreadySend = True

                elif self.pacman.currectDirection == Direction.DOWN:
                    if 0.9 > (self.pacman.position[2] - math.floor(self.pacman.position[2])) > 0.8:
                        print("Sending DOWN " + self.dataToSend)
                        Network().sendData(self.dataToSend)
                        self.previousData = self.dataToSend
                        self.alreadySend = True
                
            else: 
                self.alreadySend = False
                

