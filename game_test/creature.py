import pygame

class Creature:
    def __init__(self, hp, screen, size, location, sprite_path, is_active):
        self.hp = hp
        self.screen = screen
        self.size = size
        self.location = location
                
        self.is_active = is_active
                
        self.sprite  = pygame.image.load(sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.size[0], self.size[1]))

        self.rect = pygame.Rect(self.location[0], self.location[1] , self.size[0], self.size[1])
        self.rect = self.sprite.get_rect()

        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        
        
    def set_sprite_path(self, sprite_path):
        self.sprite_path = sprite_path
        
        
    def get_sprite_path(self):
        return self.sprite_path