from mathmatics import *

class Player:
    def __init__(self, starting_position=Vector2(), max_vector=Vector2(), speed=5):
        self.position = starting_position
        self.speed = speed
        self.max_x = max_vector.x
        self.max_y = max_vector.y

    def move(self, x, y):
        self.position.x += x * self.speed
        self.position.y += y * self.speed

        self.handle_constraints()

    def handle_constraints(self):
        if self.position.x < 0:
            self.position.x = 0
        
        if self.position.x > self.max_x:
            self.position.x = self.max_x
        
        if self.position.y < 0:
            self.position.y = 0
        
        if self.position.y > self.max_y:
            self.position.y = self.max_y