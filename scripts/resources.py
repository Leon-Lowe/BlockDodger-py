import pygame
from pygame.locals import *

class Resources:
    def __init__(self):
        #Screen Settings
        self.BACKGROUND_COLOUR = (100, 100, 100)
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 720

        #Pixel Settings
        self.PIXEL_SIZE = 40

        #Player Settings
        self.PLAYER_SPRITE_PATH = "Resources/player.png"
        self.PLAYER_WIDTH = 40
        self.PLAYER_HEIGHT = 40
        self.PLAYER_SPEED = 5

        #Enemy Settings
        self.ENEMY_SPRITE_PATH = "Resources/enemy.png"
        self.ENEMY_WIDTH = 40
        self.ENEMY_HEIGHT = 40
        self.ENEMY_SPEED = 3
        self.ENEMY_MAX_SPEED = 6
        self.ENEMY_GAP = 20

        #Enemy Manager Settings
        self.MAX_ENEMIES = 8