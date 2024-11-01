import pygame
from player import Player
from color import Color
from goblin import Goblin
from dialogue_box import DialogueBox

'''

COISAS PARA FAZER:

    - SISTEMA DE DIALOGO
    - IA PARA OS PERSONAGENS
    - SISTEMA DE INVENTARIO
    - SISTEMA DE LUTA
    
'''

pygame.init()

# DRAW OBJECTS SPRITES ETC IN SCREEN
def draw_screen():
    bg = pygame.image.load("./images/sexo.png")

#INSIDE OF THE GAME LOOP
    screen.blit(bg, (0, 0))
    
    screen.blit(p1.get_sprite(), p1.rect)
    screen.blit(g1.get_sprite(), g1.rect)
    screen.blit(db_g1.get_render(), db_g1.rect)
    

def show_dialogue_box():
    if p1.rect.colliderect(g1):
        db_g1.ative_in_screen(screen, Color(102, 102, 255))
        

# CONFIG SCREEN ON GAME
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Game Test Alpha')

# PLAYER OBJECT SET
p1 = Player([44, 54], [400, 400], 5)

# GOBLIN OBJECT SET
g1 = Goblin([44, 54], [400, 100], 2, 5)

# CREATE A DIALOGUE BOX
text = 'Teste!'
db_g1 = DialogueBox(screen_size, 400, 200, text, Color(51, 0, 0))

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
    
    p1.move_player(screen, screen_size, p1.rect)
    show_dialogue_box()
    
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()