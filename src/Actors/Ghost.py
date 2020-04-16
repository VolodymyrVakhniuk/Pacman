from Actors.Actor import Actor
from Actors.Maze import Maze
from Actors.Direction import Direction

from Util.Timer import Timer
import pyrr

from enum import Enum

class Ghost(Actor):

    class GhostColor(Enum):
        RED = 0,
        ORANGE = 1,
        PURPLE = 2,
        GREEN = 3
    
    # assume position is 2d vector (x cell, z cell)
    def __init__(self, position : list, direction : Direction, speed : float, id : str, ghostColor : GhostColor):
        
        super().__init__(position, direction, speed, id)
        self.ghostColor = ghostColor

        # 0 - LEFT
        # 1 - UP
        # 2 - RIGHT
        # 3 - DOWN
        # [ 2, 0, 2, 2, 0
        # , 0, 1, 1, 0, 1
        # , 1, 3, 0, 0, 1
        # , 1, 3, 1, 2, 2
        # , 3, 3, 2, 3, 3
        # , 3, 0, 2, 3, 3]

        self.randomList = [
            Direction.DOWN, Direction.RIGHT, Direction.DOWN, Direction.RIGHT, Direction.LEFT,
            Direction.LEFT, Direction.UP, Direction.UP, Direction.LEFT, Direction.UP,
            Direction.UP, Direction.DOWN, Direction.LEFT, Direction.LEFT, Direction.UP,
            Direction.UP, Direction.DOWN, Direction.UP, Direction.RIGHT, Direction.RIGHT,
            Direction.DOWN, Direction.DOWN, Direction.RIGHT, Direction.DOWN, Direction.DOWN,
            Direction.DOWN, Direction.LEFT, Direction.RIGHT, Direction.RIGHT, Direction.DOWN,
        ]

        self.randomListIndex = 0

        self.updateTimer = Timer()
        self.updateTimer.restart()

        self.setTurnSignal(self.randomList[self.randomListIndex])
        self.randomListIndex += 1

        self.isOnIntersectionFirst = False


    def update(self, maze : Maze):

        deltaTime = self.updateTimer.getElapsedTime()
        distance = deltaTime * self.speed
        self.updateTimer.restart()

        if maze.isIntersection(Maze.worldCoordsToCellCoords(self.position), self.currectDirection):
            if self.isOnIntersectionFirst == True:
                if self.canApplyTurnSignal(maze):
                    self.applyTurnSignal()
                    self.__setNextTurnSignal()
                    self.isOnIntersectionFirst = False
                else:
                    self.__setNextTurnSignal()
        else:
            self.isOnIntersectionFirst = True

        
        currentCellPos = Maze.worldCoordsToCellCoords(self.position)
        if not maze.isVacantSpotInSpecifiedDirection(currentCellPos, self.currectDirection) and maze.isTheMiddleOfTheCell(self.position, self.currectDirection):
            self.isMoving = False
            return

        self.position += self.frontVector * pyrr.Vector3([distance, distance, distance])

        

    def __setNextTurnSignal(self):

        while(True):
            next_direction = self.randomList[self.randomListIndex % len(self.randomList)]
            self.randomListIndex += 1

            if self.__shouldUseTurnSignal(next_direction):
                self.setTurnSignal(next_direction)
                return


    def __shouldUseTurnSignal(self, direction : Direction):

        if self.currectDirection == Direction.LEFT:
            if direction == Direction.RIGHT:
                return False
            return True

        if self.currectDirection == Direction.UP:
            if direction == Direction.DOWN:
                return False
            return True
        
        if self.currectDirection == Direction.RIGHT:
            if direction == Direction.LEFT:
                return False
            return True
        
        if self.currectDirection == Direction.DOWN:
            if direction == Direction.UP:
                return False
            return True

        return False