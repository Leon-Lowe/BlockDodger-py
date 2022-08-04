#import pygame
#from pygame.locals import *
from resources import *
from player import *

class Game:
    def __init__(self):
        pygame.init()
        self.resources = Resources()
        self.surface = pygame.display.set_mode((self.resources.SCREEN_WIDTH, self.resources.SCREEN_HEIGHT))
        self.load_resources()
        self.running = False
        self.clock = pygame.time.Clock()
        self.player = Player(self.resources.SCREEN_WIDTH - self.resources.PLAYER_WIDTH, self.resources.SCREEN_HEIGHT - self.resources.PLAYER_HEIGHT)

    def load_resources(self):
        self.player_sprite = pygame.image.load(self.resources.PLAYER_SPRITE_PATH).convert()

    def draw_call(self):
        self.surface.fill((self.resources.BACKGROUND_COLOUR))
        self.surface.blit(self.player_sprite, (self.player.x, self.player.y))
        pygame.display.update()

    def input(self):
        for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

        self.keys = pygame.key.get_pressed()

        x_move = (self.keys[pygame.K_d] - self.keys[pygame.K_a])
        y_move = (self.keys[pygame.K_s] - self.keys[pygame.K_w])

        self.player.move(x=x_move, y=y_move)

    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(60)
            self.draw_call()
            self.input()