#import pygame
#from pygame.locals import *
from resources import *
from entities.player import Player
from entities.enemy import Enemy
from mathamatics import *

class Game:
    def __init__(self):
        self.game_setup()
        self.player_setup()
        self.temp_enemy_setup()
        

    def game_setup(self):
        pygame.init()
        self.resources = Resources()
        self.surface = pygame.display.set_mode((self.resources.SCREEN_WIDTH, self.resources.SCREEN_HEIGHT))
        self.load_resources()
        self.running = False
        self.clock = pygame.time.Clock()

    def player_setup(self):
        max_x = self.resources.SCREEN_WIDTH - self.resources.PLAYER_WIDTH
        max_y = self.resources.SCREEN_HEIGHT - self.resources.PLAYER_HEIGHT
        max_vector = Vector2(max_x, max_y)
        starting_position = Vector2(self.resources.SCREEN_WIDTH/2 - self.resources.PLAYER_WIDTH, self.resources.SCREEN_HEIGHT/2 - self.resources.PLAYER_HEIGHT)
        self.player = Player(starting_position, max_vector, self.resources.PIXEL_SIZE, self.resources.PLAYER_SPEED)

    def temp_enemy_setup(self):
        starting_position = Vector2(0 + self.resources.ENEMY_GAP, 0 - self.resources.ENEMY_HEIGHT)
        self.enemy = Enemy(starting_position, self.resources.SCREEN_HEIGHT, self.resources.ENEMY_HEIGHT, self.resources.PIXEL_SIZE, self.resources.ENEMY_SPEED)

    def load_resources(self):
        self.player_sprite = pygame.image.load(self.resources.PLAYER_SPRITE_PATH).convert_alpha()
        self.enemy_sprite = pygame.image.load(self.resources.ENEMY_SPRITE_PATH).convert_alpha()

    def draw_call(self):
        self.surface.fill((self.resources.BACKGROUND_COLOUR))
        self.surface.blit(self.player_sprite, (self.player.transform.position.x, self.player.transform.position.y))
        self.surface.blit(self.enemy_sprite, (self.enemy.transform.position.x, self.enemy.transform.position.y))
        pygame.display.update()

    def input(self):
        for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

        self.keys = pygame.key.get_pressed()

    def logic(self):
        x_move = (self.keys[pygame.K_d] - self.keys[pygame.K_a])
        y_move = (self.keys[pygame.K_s] - self.keys[pygame.K_w])
        move_vector = Vector2(x_move, y_move)

        self.player.move(move_vector=move_vector)
        self.enemy.move(move_vector=Vector2(0,1))

    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(60)
            self.draw_call()
            self.input()
            self.logic()