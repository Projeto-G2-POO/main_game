import pygame

from color import Color

class Life:
    def __init__(self, location, number):
        self.location = location
        self.number = number

        self.font = pygame.font.Font(None, 30)
        self.surface = self.font.render(f'HP: {self.number}', False, Color.white())
        
    
    def update_player_life(self, player_life, screen):
        self.surface = self.font.render(f'HP: {player_life}', False, Color.white())
        screen.surface.blit(self.surface, self.location)