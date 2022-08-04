import pygame
from pygame.locals import *

class Resources:
    def __init__(self):
        self.BACKGROUND_COLOUR = (100, 100, 100)
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 720

        self.PLAYER_SPRITE_PATH = "Resources/block.jpg"
        self.PLAYER_WIDTH = 40
        self.PLAYER_HEIGHT = 40