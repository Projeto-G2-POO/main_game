import pygame

from color import Color

class Text:
    def __init__(self, location, number, text_type):
        self.location = location
        self.number = number

        self.text_type = text_type
        
        self.font = pygame.font.Font(None, 30)
        self.surface = self.font.render(f'TEXT TEMP', False, Color.white())
        
    
    def text_update(self, text_number, screen):
        
        if self.text_type == 'player_hp':
            self.surface = self.font.render(f'HP: {text_number}', False, Color.white())
        elif self.text_type == 'player_deaths':
            self.surface = self.font.render(f'DEATHS: {text_number}', False, Color.white())
        elif self.text_type == 'player_enemies_deaths':
            self.surface = self.font.render(f'KILLS: {text_number}', False, Color.white())
        
        screen.surface.blit(self.surface, self.location)
