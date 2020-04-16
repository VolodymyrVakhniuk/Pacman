import abc
from Actors.Actor import Actor
from Actors.Direction import Direction


class Command:
    @abc.abstractmethod
    def execute(self, actor : Actor):
        raise NotImplementedError


class MoveLeft(Command):
    def execute(self, actor : Actor):
        actor.setTurnSignal(Direction.LEFT)


class MoveUp(Command):
    def execute(self, actor : Actor):
        actor.setTurnSignal(Direction.UP)


class MoveRight(Command):
    def execute(self, actor : Actor):
        actor.setTurnSignal(Direction.RIGHT)


class MoveDown(Command):
    def execute(self, actor : Actor):
        actor.setTurnSignal(Direction.DOWN)