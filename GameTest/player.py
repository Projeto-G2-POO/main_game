import pygame
from creature import Creature

class Player(Creature):
    def __init__(self, size, location, veloc):
        super().__init__(size, location, sprite_path='.\GameTest\sprites\player_sprite.png')
        self.veloc = veloc
        
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        
    def change_player_sprite(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.set_sprite_path('.\GameTest\sprites\player_sprite_left.png')
                self.player_sprite_load_image()
            
            if event.key == pygame.K_d:
                self.set_sprite_path('.\GameTest\sprites\player_sprite_right.png')
                self.player_sprite_load_image()
                
            if event.key == pygame.K_w:
                self.set_sprite_path('.\GameTest\sprites\player_sprite_up.png')
                self.player_sprite_load_image()
            
            if event.key == pygame.K_s:
                self.set_sprite_path('.\GameTest\sprites\player_sprite.png')
                self.player_sprite_load_image()
                
    def player_sprite_load_image(self):
        self.sprite  = pygame.image.load(self.sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.size[0], self.size[1]))
    
    
    def move_player(self, screen, screen_size, player):
        keys = pygame.key.get_pressed()
        
        player.x += (keys[pygame.K_d] - keys[pygame.K_a]) * self.veloc
        player.y += (keys[pygame.K_s] - keys[pygame.K_w]) * self.veloc

        player.centerx = player.centerx % screen.get_width()
        player.centery = player.centery % screen.get_height()
        
        if player.x < 0:
            player.x = 0
        
        if player.x + self.size[0] > screen_size[0]:
            player.x = screen_size[0] - self.size[0]
        
        if player.y < 0:
            player.y = 0
        
        if player.y + self.size[1] > screen_size[1]:
            player.y = screen_size[1] - self.size[1]