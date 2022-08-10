import pygame
from pygame.locals import *

class Resources:
    def __init__(self):
        #Colour Settings
        self.BACKGROUND_COLOUR = (100, 100, 100)
        self.MAIN_FONT_COLOUR = (61, 61, 61)
        self.SECONDARY_FONT_COLOUR = (143, 143, 143)

        #Screen Settings
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 720

        #Pixel Settings
        self.PIXEL_SIZE = 40

        #Font Settings
        self.MAIN_FONT_PATH = "Resources/Fonts/kenney_pixel_square.ttf"

        #Player Settings
        self.PLAYER_SPRITE_PATH = "Resources/Images/player.png"
        self.PLAYER_WIDTH = 40
        self.PLAYER_HEIGHT = 40
        self.PLAYER_SPEED = 5

        #Enemy Settings
        self.ENEMY_SPRITE_PATH = "Resources/Images/enemy.png"
        self.ENEMY_WIDTH = 40
        self.ENEMY_HEIGHT = 40
        self.ENEMY_SPEED = 3
        self.ENEMY_MAX_SPEED = 6
        self.ENEMY_GAP = 20

        #Enemy Manager Settings
        self.MAX_ENEMIES = 8