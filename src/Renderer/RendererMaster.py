from Camera import Camera

from Core.MazeCore import MazeCore
from Core.PacmanCore import PacmanCore
from Core.GhostCore import GhostCore
from Core.FruitCore import FruitCore
from Core.PlatformCore import PlatformCore

from Actors.Fruits import Fruits
from Actors.Pacman import Pacman
from Actors.Ghost import Ghost

from Shaders.ColoredObjectShader import ColoredObjectShader
from Shaders.TexturedObjectShader import TexturedObjectShader
from Shaders.InstancingShader import InstancingShader

from Actors.ActorsController import ActorsController


class RendererMaster:

    def __init__(self):

        self.coloredObjectShader = ColoredObjectShader()
        self.texturedObjectShader = TexturedObjectShader()
        self.instancingShader = InstancingShader()

        self.mazeCore = MazeCore(self.coloredObjectShader)
        self.platfromCore = PlatformCore(self.texturedObjectShader)
        self.fruitCore = None#FruitCore(self.instancingShader)
    
        self.pacmanCore = PacmanCore(self.coloredObjectShader)
        self.ghostCore = GhostCore(self.coloredObjectShader)


    def addPresentComponents(self, actorsController : ActorsController):

        if actorsController.player_1_pacman:
            self.__addPacman(actorsController.player_1_pacman)
        
        if actorsController.player_2_pacman:
            self.__addPacman(actorsController.player_2_pacman)

        for ghost in actorsController.ghosts:
            self.__addGhost(ghost)


    def setFruits(self, fruits : Fruits):
        self.fruitCore = FruitCore(self.instancingShader, fruits)


    def render(self, window, camera : Camera):

        self.fruitCore.update()
        
        self.instancingShader.bind()
        self.fruitCore.render(camera, self.instancingShader)

        self.coloredObjectShader.bind()
        self.ghostCore.render(camera, self.coloredObjectShader)
        self.pacmanCore.render(camera, self.coloredObjectShader)

        self.texturedObjectShader.bind()
        self.platfromCore.render(camera, self.texturedObjectShader)

        self.coloredObjectShader.bind()
        self.mazeCore.render(camera, self.coloredObjectShader)


    def __addPacman(self, pacman):
        self.pacmanCore.addPacman(pacman)


    def __addGhost(self, ghost):
        self.ghostCore.addGhost(ghost)





