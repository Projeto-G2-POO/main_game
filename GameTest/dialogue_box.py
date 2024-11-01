import pygame
from color import Color

class DialogueBox:
    def __init__(self, screen_size, width, height, text, text_color):
        self.screen_size = screen_size
        
        self.width = width
        self.height = height
        
        self.x = (screen_size[0] - width) // 2
        self.y = (screen_size[1] - height) // 2
    
        self.text = text
        self.text_color= text_color
        
        self.font = pygame.font.Font(None, 24)
        
        self.render = self.font.render(self.text, True, self.text_color.rgb)
        self.rect = self.render.get_rect(center=(self.screen_size[0] + self.width // 2, self.screen_size[1] + self.height // 2))
    
    def ative_in_screen(self, screen, color):
        pygame.draw.rect(screen, color.rgb, (self.x, self.y, self.width, self.height))

    
    def get_render(self):
        return self.render