from mathamatics import *
from transform import *

class Enemy:
    def __init__(self, starting_position=Vector2(), max_y=100, height=40, pixel_size=0, speed=5):
        self.transform = Transform(position=starting_position)
        self.speed = speed
        self.pixel_size = pixel_size
        self.max_y = max_y
        self.height = height

    def move(self, move_vector=Vector2(0,0)):
        self.transform.move(move_vector=Vector2(move_vector.x*self.speed, move_vector.y*self.speed))

        if self.transform.position.y > self.max_y:
            self.respawn(spawn_position=Vector2(self.transform.position.x, 0 - self.height))

    def respawn(self, spawn_position=Vector2()):
        self.transform.position = spawn_position