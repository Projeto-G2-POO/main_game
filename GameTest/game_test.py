import pygame
import player
import color

pygame.init()

def draw_screen():
    screen.fill(color.Color(0, 0, 0).rgb)
    pygame.draw.rect(screen, p1.color.rgb, player)


def move_player():
    keys = pygame.key.get_pressed()
    
    player.x += (keys[pygame.K_d] - keys[pygame.K_a]) * p1.veloc
    player.y += (keys[pygame.K_s] - keys[pygame.K_w]) * p1.veloc

    player.centerx = player.centerx % screen.get_width()
    player.centery = player.centery % screen.get_height()
    

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Game Test Alpha')

p1 = player.Player([20, 20], [15, 15], color.Color(255, 0, 0), 5)
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