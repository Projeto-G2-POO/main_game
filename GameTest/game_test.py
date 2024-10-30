import pygame
from player import Player
from color import Color

pygame.init()

def draw_screen():
    screen.fill(Color.black())
    pygame.draw.rect(screen, p1.color, player)


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
    
    
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Game Test Alpha')

p1 = Player([50, 50], [200, 200], Color.red(), 5)
player = pygame.Rect(p1.location[0], p1.location[1] , p1.size[0], p1.size[1])

run_game = True

clock = pygame.time.Clock()

while run_game:
    draw_screen()
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    
    move_player()
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()