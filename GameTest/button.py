import pygame

class Button:
    def __init__(self, x, y, color, width, height, text):
        self.x = x
        self.y = y
        
        self.width = width
        self.height = height
        
        self.color = color.rgb
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    
    def set_text(self, text):
        self.text = text
    
    
    def show_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)