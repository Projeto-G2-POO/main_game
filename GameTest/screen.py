import pygame

class Screen:
    def __init__(self):
        self.screen_size = (800, 800)
        
        self.surface = pygame.display.set_mode(self.screen_size)
        
        self.background= pygame.image.load("./images/bg.png")
        
        
    def get_background(self):
        return self.background