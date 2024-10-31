import pygame
from player import Player
from color import Color
from goblin import Goblin

pygame.init()

# DRAW OBJECTS SPRITES ETC IN SCREEN
def draw_screen():
    screen.fill(Color(0, 140, 0).rgb)
    
    screen.blit(p1.get_sprite(), player)
    screen.blit(g1.get_sprite(), goblin)
    
    
# CONFIG SCREEN ON GAME
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)


# GAME NAME IN SCREEN
pygame.display.set_caption('Game Test Alpha')


# PLAYER OBJECT SETS
p1 = Player([44, 54], [400, 400], 5)
player = pygame.Rect(p1.location[0], p1.location[1] , p1.size[0], p1.size[1])
player = p1.get_sprite().get_rect()


player.x = p1.location[0]
player.y = p1.location[1]


g1 = Goblin([44, 54], [400, 800], 2, 5)
goblin = pygame.Rect(g1.location[0], g1.location[1], g1.size[0], g1.size[1])
goblin = g1.get_sprite().get_rect()

# GAME IMPORT VARIAVELS
run_game = True
clock = pygame.time.Clock()

while run_game:
    draw_screen()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    
        p1.change_player_sprite(event)
    
    g1.chase_player(player, goblin)
    p1.move_player(screen, screen_size, player)
    
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()