import abc
from Actors.Actor import Actor


class Command:
    @abc.abstractmethod
    def execute(self, actor : Actor):
        raise NotImplementedError


class MoveLeft(Command):
    def execute(self, actor : Actor):
        actor.setTurnSignal(Actor.Direction.LEFT)


class MoveUp(Command):
    def execute(self, actor : Actor):
        actor.setTurnSignal(Actor.Direction.UP)


class MoveRight(Command):
    def execute(self, actor : Actor):
        actor.setTurnSignal(Actor.Direction.RIGHT)


class MoveDown(Command):
    def execute(self, actor : Actor):
        actor.setTurnSignal(Actor.Direction.DOWN)