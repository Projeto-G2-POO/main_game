import time
import pygame
import random

from player import Player
from goblin import Goblin

from color import Color
from screen import Screen
from dialogue_box import DialogueBox

'''

COISAS PARA FAZER:

    - IA PARA OS PERSONAGENS
    - SISTEMA DE INVENTARIO
    
'''

# DRAW OBJECTS IN SCREEN
def draw_screen():
    screen.get_background()

    screen.surface.blit(screen.background, (0, 0))
    
    screen.object_in_screen(g1)
    screen.object_in_screen(p1)
    
    for enemie in enemies:
        screen.object_in_screen(enemie)
        enemie.chase_player(p1)
        
    for sphere in spheres:
        screen.object_in_screen(sphere)
        sphere.move_sphere(spheres, sphere)
        sphere.colide_with_enemies(enemies)


def fase():
    if db_g1.fase_active:
        g1.is_active = False
        
        # CRIAR SISTEMA PARA TERMINAR A FASE DEPOIS DE MATAR
        # CERTA QUANTIDADE DE INIMIGOS
        
        if pygame.time.get_ticks() % 100 == 0 and len(enemies) < 10:
            screen.create_goblin(enemies)
        
        if len(enemies) > 10:
            db_g1.fase_active = False
    

# INIT PYGAME
pygame.init()

# CREATE OBJECT SCREEN
screen = Screen()

# LIST OF ENEMIES AND SPHERES IN GAME
enemies = []
spheres = []

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
        p1.throw_sphere(event, spheres)
        
        screen.check_enemies(enemies)
            
    db_g1.show_dialogue(p1, g1, events)
    p1.move_player()
    
    fase()
    
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()