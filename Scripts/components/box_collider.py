from mathamatics import *

class BoxCollider:
    def __init__(self, position=Vector2(), pixel_size=40):
        self.position = position
        self.pixel_size = pixel_size

    def is_colliding(self, other_position=Vector2()):
        x_colliding = False
        y_colliding = False

        if ((self.position.x >= other_position.x and self.position.x < (other_position.x + self.pixel_size)) 
        or ((self.position.x + self.pixel_size) >= other_position.x and (self.position.x + self.pixel_size) < (other_position.x + self.pixel_size))):
            x_colliding = True

        if ((self.position.y >= other_position.y and self.position.y < (other_position.y + self.pixel_size)) 
        or ((self.position.y + self.pixel_size) >= other_position.y and (self.position.y + self.pixel_size) < (other_position.y + self.pixel_size))):
            y_colliding = True

        if y_colliding and x_colliding:
            return True
