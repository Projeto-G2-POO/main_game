import pygame

class Creature:
    def __init__(self, size, location, sprite_path):
        self.size = size
        self.location = location
        
        self.sprite  = pygame.image.load(sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.size[0], self.size[1]))

        self.rect = pygame.Rect(self.location[0], self.location[1] , self.size[0], self.size[1])
        self.rect = self.get_sprite().get_rect()

    def set_sprite_path(self, sprite_path):
        self.sprite_path = sprite_path
        
        
    def get_sprite_path(self):
        return self.sprite_path


    def set_sprite(self, sprite):
        self.sprite = sprite
    
        
    def get_sprite(self):
        return self.sprite