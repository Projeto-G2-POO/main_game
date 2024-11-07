import pygame
import random

from datetime import datetime

from goblin import Goblin
from hobgoblin import Hobgoblin

class Screen:
    def __init__(self):
        self.screen_size = (800, 800)
        self.surface = pygame.display.set_mode(self.screen_size)
        self.background= pygame.image.load("./images/bg.png")
        
        
    def get_background(self):
        return self.background
    
    
    def object_in_screen(self, creature):
        if creature.is_active:
            self.surface.blit(creature.sprite, creature.rect)
            
          
    @staticmethod  
    def check_enemies(enemies, player):
        for enemie in enemies:
            enemie.check_hp(enemie, player)
            
    
    @staticmethod 
    def random_coords():
        random.seed(datetime.now().timestamp())
        
        random_y = random.uniform(50, 700)
        
        if random.uniform(1, 10) > 5:
            random_x = random.uniform(10, 200)
        else:
            random_x = random.uniform(600, 750)
            
        return [random_x, random_y]
    
    
    def create_enemy(self, enemies, veloc, enemy_type):
        coords_list = self.random_coords()
        
        if enemy_type == 'goblin':
            
            enemies.append(Goblin(self, [44, 54], [coords_list[0], coords_list[1]], veloc, 1))
            
        elif enemy_type == 'hobgoblin':
            
            enemies.append(Hobgoblin(self, [44, 54], [coords_list[0], coords_list[1]], veloc, 2))