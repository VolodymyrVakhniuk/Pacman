from Camera import Camera
from Actors.MazeCore import MazeCore
from Actors.Platform import Platform
from Actors.Pacman import Pacman
from Actors.PacmanCore import PacmanCore


class RendererMaster:

    def __init__(self):

        self.maze = MazeCore()
        self.pacmanCore = PacmanCore()
        self.platfrom = Platform()
    

    def addPacmans(self, *pacmans : Pacman):

        for pacman in pacmans:
            self.pacmanCore.addPacman(pacman)

    def addGhosts(self, *ghost):
        pass


    def render(self, window, camera : Camera):

        self.pacmanCore.render(camera)
        self.platfrom.render(camera)
        self.maze.render(camera)





