import pygame
from color import Color
from pygame_widgets.button import Button

class DialogueBox:
    def __init__(self,screen_size ,box_width, box_height):
        self.screen_size = screen_size
        self.box_width = box_width
        self.box_height = box_height
        self.box_x = (screen_size[0] - box_width) // 2
        self.box_y = (screen_size[1] - box_height) - 40
        
    
    def set_text(self, text, color_text):
        self.text = text
        self.color_text = color_text
    
    
    def set_dialogue(self, screen, box_color):
        self.render = pygame.font.Font(None, 24).render(self.text, True, self.color_text)
        self.rect = self.render.get_rect(center=(self.box_x + self.box_width // 2, self.box_y + self.box_height // 2))
        
        pygame.draw.rect(screen, box_color, (self.box_x, self.box_y, self.box_width, self.box_height))
        
    
    def show_dialogue(self, object_player, object_goblin, screen, events):
        if object_player.rect.colliderect(object_goblin):
            self.set_dialogue(screen, Color(0, 92, 83).rgb)
            screen.blit(self.render, self.rect)
            self.update_dialogue_button(events)
            
    
    def show_dialogue_button(self, screen):
        text_start = 'Começar jogo'
        self.button = Button(
            screen, self.box_x, self.box_y - self.box_height, self.box_width, self.box_height,
            text=text_start,
            fontSize=24, margin=20,
            inactiveColour=Color.green(),
            pressedColour=Color.red(),
            radius=0,
            onClick=lambda: print('Funcionou!')
        )
        
        
    def update_dialogue_button(self, events):
        self.button.listen(events)
        self.button.draw()
        pygame.display.update()