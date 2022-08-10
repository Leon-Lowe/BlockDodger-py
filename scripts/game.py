#import pygame
#from pygame.locals import *
from random import randint
from resources import *
from entities.player import Player
from entities.enemy_cluster import EnemyManager
from mathamatics import *
from entities.enemy import Enemy

class Game:
    def __init__(self):
        self.game_setup()
        self.player_setup()
        self.enemy_setup()
        self.score_setup()
        self.play_background_music()

    def reset_game(self):
        self.game_over = False
        self.player_setup()
        self.enemy_setup()
        self.score_setup()
        

    def game_setup(self):
        pygame.init()
        pygame.mixer.init()

        self.resources = Resources()
        self.surface = pygame.display.set_mode((self.resources.SCREEN_WIDTH, self.resources.SCREEN_HEIGHT))
        pygame.display.set_caption("Astroid Dodger")
        self.load_resources()
        self.running = False
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.in_main_menu = True

    def player_setup(self):
        max_x = self.resources.SCREEN_WIDTH - self.resources.PLAYER_WIDTH
        max_y = self.resources.SCREEN_HEIGHT - self.resources.PLAYER_HEIGHT
        max_vector = Vector2(max_x, max_y)
        starting_position = Vector2((self.resources.SCREEN_WIDTH/2) - (self.resources.PLAYER_WIDTH/2), self.resources.SCREEN_HEIGHT - 120)
        self.player = Player(starting_position, max_vector, self.resources.PIXEL_SIZE, self.resources.PLAYER_SPEED)

    def enemy_setup(self):
        self.enemy_speed_multiplier = float(1)
        starting_position = Vector2(0 + self.resources.ENEMY_GAP, 0 - self.resources.ENEMY_HEIGHT)
        self.enemy_manager = EnemyManager(Enemy(), self.resources.MAX_ENEMIES, starting_position, self.resources.ENEMY_GAP, self.resources.SCREEN_HEIGHT, self.resources.PIXEL_SIZE, self.resources.ENEMY_SPEED)

    def score_setup(self):
        self.score = 0
        self.load_fonts()

    def load_fonts(self):
        self.score_font = pygame.font.Font(self.resources.MAIN_FONT_PATH, 300)
        self.title_font = pygame.font.Font(self.resources.MAIN_FONT_PATH, 60)
        self.secondary_font = pygame.font.Font(self.resources.MAIN_FONT_PATH, 30)

    def load_resources(self):
        self.player_sprite = pygame.image.load(self.resources.PLAYER_SPRITE_PATH).convert_alpha()
        self.enemy_sprite = pygame.image.load(self.resources.ENEMY_SPRITE_PATH).convert_alpha()

    def draw_call(self):
        if self.game_over == False and self.in_main_menu == False:
            self.draw_game()
        
        if self.game_over == True and self.in_main_menu == False:
            self.draw_game_over()
        
        if self.in_main_menu == True:
            self.draw_main_menu()

        pygame.display.update()

    def draw_game(self):
        self.surface.fill((self.resources.BACKGROUND_COLOUR))

        self.score_text = self.score_font.render(f"{self.score}", True, self.resources.SECONDARY_FONT_COLOUR)
        self.score_text_rect = self.score_text.get_rect(center=((self.resources.SCREEN_WIDTH/2) + (self.resources.PIXEL_SIZE/2), self.resources.SCREEN_HEIGHT/2))
        self.surface.blit(self.score_text, self.score_text_rect)

        self.surface.blit(self.player_sprite, (self.player.transform.position.x, self.player.transform.position.y))

        for i in range(len(self.enemy_manager.enemies)):
            new_enemy_sprite = self.enemy_sprite
            new_enemy_sprite = pygame.transform.rotate(new_enemy_sprite, self.enemy_manager.enemies[i].rotation)
            self.surface.blit(new_enemy_sprite, (self.enemy_manager.enemies[i].transform.position.x, self.enemy_manager.enemies[i].transform.position.y))

    def draw_main_menu(self):
        self.surface.fill((self.resources.BACKGROUND_COLOUR))

        title_text_one = self.title_font.render(f"Asteroid", True, self.resources.MAIN_FONT_COLOUR)
        title_text_rect = title_text_one.get_rect(center=(self.resources.SCREEN_WIDTH/2, 60))
        self.surface.blit(title_text_one, title_text_rect)

        title_text_two = self.title_font.render(f"Dodger", True, self.resources.MAIN_FONT_COLOUR)
        title_text_rect = title_text_two.get_rect(center=(self.resources.SCREEN_WIDTH/2, 120))
        self.surface.blit(title_text_two, title_text_rect)

        sub_text_one = self.secondary_font.render(f"Press 'enter' to play", True, self.resources.SECONDARY_FONT_COLOUR)
        sub_text_one_rect = sub_text_one.get_rect(center=(self.resources.SCREEN_WIDTH/2, (self.resources.SCREEN_HEIGHT/2)))
        self.surface.blit(sub_text_one, sub_text_one_rect)
    
    def draw_game_over(self):
        self.surface.fill((self.resources.BACKGROUND_COLOUR))

        title_text = self.title_font.render(f"You Died!", True, self.resources.MAIN_FONT_COLOUR)
        title_text_rect = title_text.get_rect(center=(self.resources.SCREEN_WIDTH/2, (self.resources.SCREEN_HEIGHT/2) - 60))
        self.surface.blit(title_text, title_text_rect)

        sub_text_one = self.secondary_font.render(f"You dodged {self.score} asteroids", True, self.resources.SECONDARY_FONT_COLOUR)
        sub_text_one_rect = sub_text_one.get_rect(center=(self.resources.SCREEN_WIDTH/2, (self.resources.SCREEN_HEIGHT/2)))
        self.surface.blit(sub_text_one, sub_text_one_rect)

        sub_text_two = self.secondary_font.render(f"Press 'Enter' to restart", True, self.resources.SECONDARY_FONT_COLOUR)
        sub_text_two_rect = sub_text_two.get_rect(center=(self.resources.SCREEN_WIDTH/2, self.resources.SCREEN_HEIGHT - 60))
        self.surface.blit(sub_text_two, sub_text_two_rect)

    def play_background_music(self):
        pygame.mixer.music.load("Resources/Sfx/music.mp3")
        pygame.mixer.music.set_volume(30)
        pygame.mixer.music.play(-1)
    
    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"Resources/Sfx/{sound}.wav")
        pygame.mixer.Sound.play(sound)

    def input(self):
        for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if self.game_over:
                        if event.key == K_RETURN:
                            self.play_sound("ui_select")
                            self.reset_game()
                    if self.in_main_menu:
                        if event.key == K_RETURN:
                            self.play_sound("ui_select")
                            self.in_main_menu = False

        self.keys = pygame.key.get_pressed()

    def logic(self):
        if self.game_over == False and self.in_main_menu == False:
            self.game_logic()

    def game_logic(self):
        x_move = (self.keys[pygame.K_d] - self.keys[pygame.K_a])
        #y_move = (self.keys[pygame.K_s] - self.keys[pygame.K_w])
        move_vector = Vector2(x_move, 0)

        self.player.move(move_vector=move_vector)

        for i in range(len(self.enemy_manager.enemies)):
            self.enemy_manager.enemies[i].move(move_vector=Vector2(0,1))
            if self.enemy_manager.enemies[i].collider.is_colliding(self.player.transform.position):
                self.play_sound("explosion")
                self.game_over = True

        if self.enemy_manager.reached_bottom():
            self.score += 1
            print(self.score)

            self.play_sound("score")

            if self.resources.ENEMY_SPEED * self.enemy_speed_multiplier < self.resources.ENEMY_MAX_SPEED:
                self.enemy_speed_multiplier += float(0.05)

            if self.resources.ENEMY_SPEED * self.enemy_speed_multiplier > self.resources.ENEMY_MAX_SPEED:
                self.enemy_speed_multiplier = self.resources.ENEMY_MAX_SPEED / self.resources.ENEMY_SPEED

            self.enemy_manager.spawn_enemies(self.enemy_speed_multiplier)

    def run(self):
        self.running = True

        while self.running:
            self.clock.tick(60)
            self.draw_call()
            self.input()
            self.logic()