from Actors.Pacman import Pacman
from Actors.Ghost import Ghost
from Actors.Maze import Maze
from Actors.Fruits import Fruits

from Util.Timer import Timer

from Actors.Direction import Direction


class ActorsController:

    def __init__(self):
        
        self.maze = Maze()

        self.player_1_pacman = None
        self.player_2_pacman = None

        self.ghosts = []
        self.maxNumberOfGhosts = 4

        self.fruits = Fruits(self.maze)

    
    def initializePlayer1(self, position, direction : Direction, speed : float, id : str):
        self.player_1_pacman = Pacman(position, direction, speed, id)


    def initializePlayer2(self, position, direction : Direction, speed : float, id : str):
        self.player_1_pacman = Pacman(position, direction, speed, id)


    def addGhost(self, position, direction : Direction, speed : float, id : str, ghostColor : Ghost.GhostColor):

        if len(self.ghosts) == self.maxNumberOfGhosts:
            print("Max 4 ghosts")
            return

        self.ghosts.append(Ghost(position, direction, speed, id, ghostColor))

    
    def notifyActor(self, message : str, id : str):

        if self.player_1_pacman.id == id:
            self.player_1_pacman.notify(message)
        elif self.player_2_pacman.id == id:
            self.player_2_pacman.notify(message)
        else:
            for ghost in self.ghosts:
                if ghost.id == id:
                    ghost.notify(message)


    def update(self):

        if self.player_1_pacman:
            self.player_1_pacman.update(self.maze)
        if self.player_2_pacman:
            self.player_2_pacman.update(self.maze)

        for ghost in self.ghosts:
            ghost.update(self.maze)
    
        if self.player_1_pacman:
            self.fruits.update(self.player_1_pacman)
    
        # self.fruits.update(self.player_1_pacman, self.player_2_pacman)


