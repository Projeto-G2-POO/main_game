import pygame

class DialogueBox:
    def __init__(self,screen_size ,box_width, box_height):
        self.screen_size = screen_size
        self.box_width = box_width
        self.box_height = box_height
        self.box_x = (screen_size[0] - box_width) // 2
        self.box_y = (screen_size[1] - box_height) // 2
        
    
    def set_text(self, text, color_text):
        self.text = text
        self.color_text = color_text
    
    
    def set_dialogue(self, screen, box_color):
        self.render = pygame.font.Font(None, 24).render(self.text, True, self.color_text)
        self.rect = self.render.get_rect(center=(self.box_x + self.box_width // 2, self.box_y + self.box_height // 2))
        
        pygame.draw.rect(screen, box_color, (self.box_x, self.box_y, self.box_width, self.box_height))