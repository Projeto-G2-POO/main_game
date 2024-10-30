import pygame

class Player:
    def __init__(self, size, location, color, veloc):
        self.size = size
        self.location = location
        self.color = color
        self.veloc = veloc
        
        
    def sprite_path(self, path):
        self.sprite  = pygame.image.load(path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.size[0], self.size[1]))
        
        
    def set_sprite(self, sprite):
        self.sprite = sprite
    
        
    def get_sprite(self):
        return self.sprite