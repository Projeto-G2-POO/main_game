import pygame
import random

from goblin import Goblin

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
    def check_enemies(enemies):
        for enemie in enemies:
            enemie.check_hp(enemie)
            
            
    def create_goblin(self, enemies):
        random_y = random.uniform(50, 700)
            
        if random.uniform(1, 2) == 1:
            random_x = random.uniform(10, 200)
        else:
            random_x = random.uniform(600, 750)
            
        enemies.append(Goblin(self, [44, 54], [random_x, random_y], 2, 1))