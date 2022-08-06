from mathamatics import *
from transform import *

class Player:
    def __init__(self, starting_position=Vector2(), max_vector=Vector2(), pixel_size=0, speed=5):
        self.transform = Transform(position=starting_position)
        self.speed = speed
        self.max_x = max_vector.x
        self.max_y = max_vector.y
        self.pixel_size = pixel_size

    def move(self, move_vector=Vector2(0,0)):
        self.transform.move(move_vector=Vector2(move_vector.x*self.speed, move_vector.y*self.speed))

        self.handle_constraints()

    def handle_constraints(self):
        if self.transform.position.x < 0:
            self.transform.position.x = 0
        
        if self.transform.position.x > self.max_x:
            self.transform.position.x = self.max_x
        
        if self.transform.position.y < 0:
            self.transform.position.y = 0
        
        if self.transform.position.y > self.max_y:
            self.transform.position.y = self.max_y