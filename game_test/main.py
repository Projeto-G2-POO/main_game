import pygame

from player import Player
from allied import Allied

from text import Text
from color import Color
from level import Level
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
    screen.surface.blit(p1_hp_text.surface, p1_hp_text.location)
    screen.surface.blit(p1_deaths_text.surface, p1_deaths_text.location)
    
    screen.object_in_screen(g_allied)
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
    if not p1.death:
        if l1.number <= 3:
            l1.power_enemy(db_g_allied, screen, pygame.time.get_ticks(), g_allied, 'goblin')
        
        if l1.number >= 4 and l1.number <= 6:
            l1.power_enemy(db_g_allied, screen, pygame.time.get_ticks(), g_allied, 'hobgoblin')
            
        if l1.number >= 7:
            l1.power_enemy(db_g_allied, screen, pygame.time.get_ticks(), g_allied, 'redcap')
    else:
        l1.reset_level(g_allied, db_g_allied)
    

# INIT PYGAME
pygame.init()

# CREATE OBJECT SCREEN
screen = Screen()

# PLAYER OBJECT SET
p1 = Player(screen, [44, 54], [400, 400], 5, 5)

# TEXT IN SCREEN
p1_hp_text = Text([30, 30], p1.hp, 'player_hp')
p1_deaths_text = Text([30, 60], p1.total_deaths, 'player_deaths')
p1_enemies_deaths = Text([30, 90], p1.enemies_deaths, 'player_enemies_deaths')

# LEVEL OBJECT SET
l1 = Level(1, 5, 1, p1)

# GOBLIN OBJECT SET
g_allied = Allied(screen, [44, 54], [400, 100])

# CREATE A DIALOGUE BOX
text_dialogue = 'Ola viajante. Seja bem vindo a esse mundo! Vamos jogar?'
db_g_allied = DialogueBox(screen, 520, 80)
db_g_allied.set_text(text_dialogue, Color.white())

# CREATE A BUTTON
db_g_allied.show_dialogue_button()

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
        
        
        screen.check_enemies(l1.enemies_list)
      
    p1_hp_text.text_update(p1.hp, screen)   
    p1_deaths_text.text_update(p1.total_deaths, screen)
    p1_enemies_deaths.text_update(p1.enemies_deaths, screen)
       
    db_g_allied.show_dialogue(p1, g_allied, events)
    p1.move_player()
    p1.check_hp()
    
    level_seletion()
    
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()