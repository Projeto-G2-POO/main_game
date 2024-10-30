import pygame
from player import Player
from color import Color

pygame.init()

# DRAW OBJECTS SPRITES ETC IN SCREEN
def draw_screen():
    screen.fill(Color(0, 140, 0).rgb)
    pygame.draw.rect(screen, p1.color, player)


# CONFIG PLAYER MOVIMENT BTN AND MOVE SET
def move_player():
    keys = pygame.key.get_pressed()
    
    player.x += (keys[pygame.K_d] - keys[pygame.K_a]) * p1.veloc
    player.y += (keys[pygame.K_s] - keys[pygame.K_w]) * p1.veloc

    player.centerx = player.centerx % screen.get_width()
    player.centery = player.centery % screen.get_height()
    
    if player.x < 0:
        player.x = 0
    
    if player.x + p1.size[0] > screen_size[0]:
        player.x = screen_size[0] - p1.size[0]
    
    if player.y < 0:
        player.y = 0
    
    if player.y + p1.size[1] > screen_size[1]:
        player.y = screen_size[1] - p1.size[1]
    

def sprite_validad():
    screen.blit(p1.get_sprite(), player)


# CONFIG SCREEN ON GAME
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)


# GAME NAME IN SCREEN
pygame.display.set_caption('Game Test Alpha')


# PLAYER OBJECT SETS
p1 = Player([34, 44], [200, 200], Color.red(), 5)
player = pygame.Rect(p1.location[0], p1.location[1] , p1.size[0], p1.size[1])


# PLAYER SPRITE CONFIG
p1.set_sprite('.\GameTest\sprites\player_sprite.png')
player = p1.get_sprite().get_rect()


# GAME IMPORT VARIAVELS
run_game = True
clock = pygame.time.Clock()

while run_game:
    draw_screen()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    
    sprite_validad()
    move_player()
    
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()