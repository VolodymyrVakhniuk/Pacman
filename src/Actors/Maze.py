from Actors.Entity import Entity
from Actors.Direction import Direction
import math
import pyrr

class Maze:

    Width = 28
    Length = 32

    def __init__(self):

        self.maze = [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
                [1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
                [1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1],
                [1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,0,1],
                [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
                [1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1],
                [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
                [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
                [1,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
                [1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1],
                [1,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1],
                [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
                [1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ]


    def isVacantSpot(self, cellCoords):
        return self.maze[cellCoords[1]][cellCoords[0]] == 0


    def isVacantSpotInSpecifiedDirection(self, cellCoords, direction : Direction):
        
        if direction == Direction.NONE:
            return self.isVacantSpot(cellCoords)

        if direction == Direction.LEFT:
            return self.isVacantSpot([cellCoords[0] - 1, cellCoords[1]])
        
        if direction == Direction.UP:
            return self.isVacantSpot([cellCoords[0], cellCoords[1] - 1])

        if direction == Direction.RIGHT:
            return self.isVacantSpot([cellCoords[0] + 1, cellCoords[1]])
        
        if direction == Direction.DOWN:
            return self.isVacantSpot([cellCoords[0], cellCoords[1] + 1])
        
   
        
    @staticmethod
    def cellCoordsToWorldCoords(cellCoords):
        
        cellMiddleBias = 0.5

        x_coord = cellCoords[0] - (Maze.Width / 2) + cellMiddleBias
        y_coord = 0.6
        z_coord = cellCoords[1] - (Maze.Length / 2) + cellMiddleBias

        return [x_coord, y_coord, z_coord]

    
    @staticmethod
    def worldCoordsToCellCoords(worldCoords):

        x_coord = int(math.floor(worldCoords[0]) + Maze.Width / 2)
        y_coord = int(math.floor(worldCoords[2]) + Maze.Length / 2)
        
        return [x_coord, y_coord]


    def isIntersection(self, cellCoords, curDirection : Direction):

        if curDirection == Direction.LEFT:
            if self.isVacantSpotInSpecifiedDirection(cellCoords, Direction.UP):
                return True
            if self.isVacantSpotInSpecifiedDirection(cellCoords, Direction.DOWN):
                return True
            return False

        if curDirection == Direction.UP:
            if self.isVacantSpotInSpecifiedDirection(cellCoords, Direction.LEFT):
                return True
            if self.isVacantSpotInSpecifiedDirection(cellCoords, Direction.RIGHT):
                return True
            return False

        if curDirection == Direction.RIGHT:
            if self.isVacantSpotInSpecifiedDirection(cellCoords, Direction.UP):
                return True
            if self.isVacantSpotInSpecifiedDirection(cellCoords, Direction.DOWN):
                return True
            return False

        if curDirection == Direction.DOWN:
            if self.isVacantSpotInSpecifiedDirection(cellCoords, Direction.LEFT):
                return True
            if self.isVacantSpotInSpecifiedDirection(cellCoords, Direction.RIGHT):
                return True
            return False

        return False
    


    @staticmethod
    def isTheMiddleOfTheCell(worldCoords, direction : Direction):

        if direction == Direction.LEFT:
            truncatedValueX = worldCoords[0] - math.floor(worldCoords[0])

            if truncatedValueX <= 0.5:
                return True

        elif direction == Direction.RIGHT:
            truncatedValueX = worldCoords[0] - math.floor(worldCoords[0])

            if truncatedValueX >= 0.5:
                return True

        elif direction == Direction.UP:
            truncatedValueX = worldCoords[2] - math.floor(worldCoords[2])

            if truncatedValueX <= 0.5:
                return True
        
        elif direction == Direction.DOWN:
            truncatedValueX = worldCoords[2] - math.floor(worldCoords[2])

            if truncatedValueX >= 0.5:
                return True

        return False

        