from entities.enemy import *
import random

class EnemyManager():
    def __init__(self, template=Enemy(), enemies_max=1, starting_position=Vector2(), enemy_gap=5, enemy_max_y=100, pixel_size=0, enemy_speed=5):
        self.enemy_template = template
        self.enemies = [Enemy()]
        self.enemies_max = enemies_max
        self.first_enemy_position = starting_position
        self.pixel_size = pixel_size
        self.enemy_speed = enemy_speed
        self.enemy_max_y = enemy_max_y
        self.enemy_gap = enemy_gap

        self.spawn_enemies()
        

    def spawn_enemies(self, speed_multiplier = float(1)):
        self.enemies.clear()
        deleted = 0

        for i in range(self.enemies_max):
            current_position = Vector2(self.first_enemy_position.x + ((self.pixel_size * i) + (self.enemy_gap * i)), self.first_enemy_position.y)
            rand_chance = random.randint(0,4)
            if rand_chance != 0:
                self.enemies.append(Enemy(current_position, self.enemy_max_y, self.pixel_size, (self.enemy_speed * speed_multiplier)))
            else:
                deleted += 1

        if deleted == 0:
            self.delete_random_enemy()

    def delete_random_enemy(self):
        for i in range(2):
            rand_position_in_enemies = random.randint(0, self.enemies_max - (1 + i))
            self.enemies.pop(rand_position_in_enemies)



    def reached_bottom(self):
        first_enemy = self.enemies[0]
        if first_enemy.reached_bottom == True:
            return True
