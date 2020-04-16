from Actors.Entity import Entity
from Actors.Maze import Maze
from Actors.Pacman import Pacman


class Fruits:

    def __init__(self, maze : Maze):
        self.fruitPositions = self.positions = [[col, row] for row in range(Maze.Length - 1) for col in range(Maze.Width) if maze.isVacantSpot([col, row])]
       
        self.firstUpdate = True
        self.prev_pacman_1_position = []
        self.prev_pacman_2_position = []

        self.fruitPositionsChanged = False


    def update(self, *pacmans : Pacman):
        
        if self.firstUpdate == True:

            self.prev_pacman_1_position = Maze.worldCoordsToCellCoords(pacmans[0].position)
            # self.prev_pacman_2_position = Maze.worldCoordsToCellCoords(pacmans[1].position)

            self.firstUpdate = False
            return
        

        pacman_positions = [self.prev_pacman_1_position, self.prev_pacman_2_position]
        position_index = 0

        self.fruitPositionsChanged = False

        for pacman in pacmans:

            curPacmanCellCoords = Maze.worldCoordsToCellCoords(pacman.position)

            if curPacmanCellCoords != self.prev_pacman_1_position:
                if curPacmanCellCoords in self.fruitPositions:
                    self.fruitPositions.remove(curPacmanCellCoords)
                    self.fruitPositionsChanged = True
            
            self.prev_pacman_1_position = curPacmanCellCoords
            

