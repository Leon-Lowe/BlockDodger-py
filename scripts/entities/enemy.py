from mathamatics import *
from components.transform import Transform
from components.box_collider import BoxCollider

class Enemy:
    def __init__(self, starting_position=Vector2(), max_y=100, pixel_size=0, speed=float(5), rotation=0):
        self.transform = Transform(position=starting_position)
        self.speed = speed
        self.pixel_size = pixel_size
        self.max_y = max_y
        self.reached_bottom = False
        self.rotation = rotation

        self.collider = BoxCollider(self.transform.position, self.pixel_size)

    def move(self, move_vector=Vector2(0,0)):
        self.transform.move(move_vector=Vector2(0, move_vector.y*self.speed))
        self.collider.position = self.transform.position

        if self.transform.position.y > self.max_y:
            self.reached_bottom = True