import glfw
from InputHandlers.Command import MoveLeft, MoveUp, MoveRight, MoveDown
from Actors.Pacman import Pacman
from Network1 import Network


class PacmanInputHandler:

    def __init__(self, pacman : Pacman):

        self.pacman = pacman

        self.buttonJ = MoveLeft()
        self.buttonI = MoveUp()
        self.buttonL = MoveRight()
        self.buttonK = MoveDown()

    
    def handleInput(self, window):

        if glfw.get_key(window, glfw.KEY_J) == glfw.PRESS:
            Network().sendData('a')
            #self.buttonJ.execute(self.pacman)

        if glfw.get_key(window, glfw.KEY_I) == glfw.PRESS:
            Network().sendData('w')
            #self.buttonI.execute(self.pacman)

        if glfw.get_key(window, glfw.KEY_L) == glfw.PRESS:
            Network().sendData('d')
            #self.buttonL.execute(self.pacman)

        if glfw.get_key(window, glfw.KEY_K) == glfw.PRESS:
            Network().sendData('s')
            #self.buttonK.execute(self.pacman)
        

        


