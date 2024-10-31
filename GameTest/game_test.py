import pygame
from player import Player
from color import Color
from goblin import Goblin

'''

COISAS PARA FAZER:

    1 - BACKGROUND (MICHAS FALOU Q VAI FAZER)
    2 - SISTEMA DE DIALOGO
    3 - IA PARA OS PERSONAGENS
    4 - SISTEMA DE INVENTARIO
    5 - SISTEMA DE LUTA
    
'''

pygame.init()

# DRAW OBJECTS SPRITES ETC IN SCREEN
def draw_screen():
    screen.fill(Color(0, 140, 0).rgb)
    
    screen.blit(p1.get_sprite(), p1.rect)
    screen.blit(g1.get_sprite(), g1.rect)
    
    
# CONFIG SCREEN ON GAME
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Game Test Alpha')

# PLAYER OBJECT SET
p1 = Player([44, 54], [400, 400], 5)

# GOBLIN OBJECT SET
g1 = Goblin([44, 54], [400, 800], 2, 5)

# GAME IMPORT VARIAVELS
run_game = True
clock = pygame.time.Clock()

# WHILE MAKE GAME RUN
while run_game:
    draw_screen()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    
        p1.change_player_sprite(event)
    
    g1.chase_player(p1.rect, g1.rect)
    p1.move_player(screen, screen_size, p1.rect)
    
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()