import pygame

pygame.init()

# inicializacao da tela
screen_size: tuple = (800, 800)
screen = pygame.display.set_mode(screen_size)

# nome jogo
pygame.display.set_caption('Game Test Alpha')

ball_size = 15
player_size = 100

blocks_line = 8
lines_blocks = 5
tot_blocks = blocks_line * lines_blocks

ball = pygame.Rect(100, 500, ball_size, ball_size)
player = pygame.Rect(0, 750, player_size, 15)

def create_blocks(blocks_line, lines_blocks):
    width_screen = screen_size[0]
    height_screen = screen_size[1]
    
    blocks_spaces = 5
    
    width_blocks = width_screen / 8 - blocks_spaces
    height_blocks = 15
    
    distance_lines = height_blocks + 10
    
    blocks = []
    
    for i in range(lines_blocks):
        for j in range(blocks_line):
            
            block = pygame.Rect(j * (width_blocks + distance_lines), i * distance_lines, width_blocks, height_blocks)
            blocks.append(block)
    
    return blocks

def draw_blocks(blocks):
    for block in blocks:
        pygame.draw.rect(screen, colors['green'], block)

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

end_game = False
points = 0
ball_move = [1, -1]

def draw_in_screen():
    screen.fill(colors['black'])
    pygame.draw.rect(screen, colors['blue'], player)
    pygame.draw.rect(screen, colors['white'], ball)


def player_move(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            if (player.x + player_size) < screen_size[0]:
                player.x = player.x + 55
            
        if event.key == pygame.K_a:
            if player.x > 0:
                player.x = player.x - 55


def ball_moviment(ball):
    moviment = ball_move
    ball.x = ball.x + moviment[0]
    ball.y = ball.y + moviment[1]
    
    if ball.x <= 0:
        moviment[0] = - moviment[0]
        
    if ball.x <= 0:
        moviment[1] = - moviment[1]
        
    if ball.x + ball_size >= screen_size[0]:
        moviment[0] = - moviment[0]
        
    if ball.y + ball_size >= screen_size[1]:
        moviment = None
        
    if player.collidepoint(ball.x, ball.y):
        moviment[1] = - moviment[1]
        
    for block in blocks:
        if block.collidepoint(ball.x, ball.y):
            blocks.remove(block)
            moviment[1] = - moviment[1]

    return moviment

blocks = create_blocks(blocks_line, lines_blocks)

while not end_game:
    draw_in_screen()
    draw_blocks(blocks)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True
        player_move(event)
        
    ball_move = ball_moviment(ball)
    
    if not ball_move:
        end_game = True
    
    pygame.time.wait(1)
    pygame.display.flip()
    
pygame.quit()