import pygame

from color import Color

class Text:
    def __init__(self, location, number, text_type):
        self.location = location
        self.number = number

        if text_type == 'player_hp':
            self.player_life()
        elif text_type == 'player_deaths':
            self.player_death()
        
    
    def player_life(self):
        self.font = pygame.font.Font(None, 30)
        self.surface = self.font.render(f'HP: {self.number}', False, Color.white())
        
    
    def player_death(self):
        self.font = pygame.font.Font(None, 30)
        self.surface = self.font.render(f'DEATHS: {self.number}', False, Color.white())
    
    
    def update_player_life(self, player_life, screen):
        self.surface = self.font.render(f'HP: {player_life}', False, Color.white())
        screen.surface.blit(self.surface, self.location)
        
    
    def update_player_deaths(self, player_deaths, screen):
        self.surface = self.font.render(f'DEATHS: {player_deaths}', False, Color.white())
        screen.surface.blit(self.surface, self.location)