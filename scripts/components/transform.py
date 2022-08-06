from mathamatics import *

class Transform:
    def __init__(self, position=Vector2(0,0), scale=Vector2(1,1), rotation=Vector2(0,0)):
        self.position = position
        self.scale = scale
        self.rotation = rotation

    def set_position(self, position=Vector2(0,0)):
        self.position = position

    def move(self, move_vector=Vector2(0,0)):
        self.position.x += move_vector.x
        self.position.y += move_vector.y
