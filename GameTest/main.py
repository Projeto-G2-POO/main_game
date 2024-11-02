import pygame

from player import Player
from goblin import Goblin

from color import Color
from screen import Screen
from dialogue_box import DialogueBox

'''

COISAS PARA FAZER:

    - SISTEMA DE DIALOGO
    - IA PARA OS PERSONAGENS
    - SISTEMA DE INVENTARIO
    - SISTEMA DE LUTA
    
'''

# DRAW OBJECTS IN SCREEN
def draw_screen():
    screen.get_background()

    screen.surface.blit(screen.background, (0, 0))
    screen.surface.blit(p1.sprite, p1.rect)
    screen.surface.blit(g1.sprite, g1.rect)


# INIT PYGAME
pygame.init()

# CREATE OBJECT SCREEN
screen = Screen()

# PLAYER OBJECT SET
p1 = Player(screen, [44, 54], [400, 400], 5)

# GOBLIN OBJECT SET
g1 = Goblin(screen, [44, 54], [400, 100], 2, 999)

# CREATE A DIALOGUE BOX
text_dialogue = 'Ola viajante. Seja bem vindo a esse mundo!\nVamos jogar?'
db_g1 = DialogueBox(screen, 390, 80)
db_g1.set_text(text_dialogue, Color.white())

# CREATE A BUTTON
db_g1.show_dialogue_button()

# GAME IMPORTANT VARIAVELS
run_game = True
clock = pygame.time.Clock()

# WHILE MAKE GAME RUN
while run_game:
    draw_screen()
    clock.tick(120)
    
    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            run_game = False
    
        p1.change_player_sprite(event)
            
    p1.move_player()
    db_g1.show_dialogue(p1, g1, events)
    
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()