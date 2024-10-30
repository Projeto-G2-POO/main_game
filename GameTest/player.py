import pygame
from creature import Creature

class Player(Creature):
    def __init__(self, size, location, veloc):
        super().__init__(size, location, veloc)
        
        
    def sprite_path(self, path):
        self.sprite  = pygame.image.load(path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.size[0], self.size[1]))
        
        
    def set_sprite(self, sprite):
        self.sprite = sprite
    
        
    def get_sprite(self):
        return self.sprite