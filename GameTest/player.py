import pygame
from creature import Creature

class Player(Creature):
    def __init__(self, size, location, veloc):
        super().__init__(size, location, sprite_path='.\GameTest\sprites\player-r.png')
        self.veloc = veloc
        
        
    def change_player_sprite(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.set_sprite_path('.\GameTest\sprites\player-l.png')
                self.player_sprite_load_image()
            
            if event.key == pygame.K_d:
                self.set_sprite_path('.\GameTest\sprites\player-r.png')
                self.player_sprite_load_image()
            
                
    def player_sprite_load_image(self):
        self.sprite  = pygame.image.load(self.sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.size[0], self.size[1]))
    
    
    def move_player(self, screen, screen_size):
        keys = pygame.key.get_pressed()
        
        self.rect.x += (keys[pygame.K_d] - keys[pygame.K_a]) * self.veloc
        self.rect.y += (keys[pygame.K_s] - keys[pygame.K_w]) * self.veloc

        self.rect.centerx = self.rect.centerx % screen.get_width()
        self.rect.centery = self.rect.centery % screen.get_height()
        
        if self.rect.x < 0:
            self.rect.x = 0
        
        if self.rect.x + self.size[0] > screen_size[0]:
            self.rect.x = screen_size[0] - self.size[0]
        
        if self.rect.y < 0:
            self.rect.y = 0
        
        if self.rect.y + self.size[1] > screen_size[1]:
            self.rect.y = screen_size[1] - self.size[1]

        if self.rect.y > 704:
            self.rect.y = 704
            

    