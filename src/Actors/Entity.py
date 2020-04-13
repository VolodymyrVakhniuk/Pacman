import pyrr
import numpy

# expect rotations in degrees
class Entity:
    def __init__(self, position, rotation):
        self.position = position
        self.rotation = rotation