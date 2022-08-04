class Player:
    def __init__(self, max_x, max_y):
        self.x = 0
        self.y = 0
        self.speed = 5
        self.max_x = max_x
        self.max_y = max_y

    def move(self, x, y):
        self.x += x * self.speed
        self.y += y * self.speed

        self.handle_constraints()

    def handle_constraints(self):
        if self.x < 0:
            self.x = 0
        
        if self.x > self.max_x:
            self.x = self.max_x
        
        if self.y < 0:
            self.y = 0
        
        if self.y > self.max_y:
            self.y = self.max_y