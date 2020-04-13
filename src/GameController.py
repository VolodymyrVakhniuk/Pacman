from Actors.Actor import Actor
from Actors.Pacman import Pacman


class GameController:

    def __init__(self):

        self.player_1_pacman = None
        self.player_2_pacman = None
        
        self.ghosts = []


    def addPacman(self, position, rotationValue : Actor.Direction, id : str, player1 : bool):

        if player1 == True:
            self.player_1_pacman = Pacman(position, rotationValue, id)

        else:
            self.player_2_pacman = Pacman(position, rotationValue, id)


    def addGhost(self, position, rotationValue : Actor.Direction, id : str):
        pass
