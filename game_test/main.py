import pygame

from player import Player
from goblin import Goblin


from life import Life
from color import Color
from levels import Level
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
    screen.surface.blit(p1_life.surface, p1_life.location)
    
    screen.object_in_screen(g1)
    screen.object_in_screen(p1)
    
    for enemie in l1.enemies_list:
        screen.object_in_screen(enemie)
        enemie.chase_player(p1)
        enemie.demage_player(p1, pygame.time.get_ticks())
        
    for sphere in p1.spheres_list:
        screen.object_in_screen(sphere)
        sphere.move_sphere(p1.spheres_list, sphere)
        sphere.colide_with_enemies(l1.enemies_list, p1)


# LEVEL SELECTION
def level_seletion():
    if l1.number <= 3:
        l1.power_enemy(db_g1, screen, pygame.time.get_ticks(), g1, 'goblin')
        
    if l1.number >= 4 and l1.number <= 6:
        l1.power_enemy(db_g1, screen, pygame.time.get_ticks(), g1, 'hobgoblin')
    

# INIT PYGAME
pygame.init()

# CREATE OBJECT SCREEN
screen = Screen()

# PLAYER OBJECT SET
p1 = Player(screen, [44, 54], [400, 400], 5, 5)
p1_life = Life([0, 0], p1.hp)

# LEVEL OBJECT SET
l1 = Level(1, 5, 1, p1)

# GOBLIN OBJECT SET
g1 = Goblin(screen, [44, 54], [400, 100], 9999, 2)

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
        p1.throw_sphere(event)
        p1_life.update_player_life(p1.hp, screen)
        
        screen.check_enemies(l1.enemies_list)
            
    db_g1.show_dialogue(p1, g1, events)
    p1.move_player()
    
    level_seletion()
    
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()
