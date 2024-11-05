import pygame

from sphere import Sphere
from creature import Creature

class Player(Creature):
    def __init__(self, screen, size, location, veloc, hp):
        super().__init__(screen, size, location, sprite_path='.\game_test\sprites\player-r.png', is_active=True)
        
        self.veloc = veloc
        self.hp = hp
        
        self.death = False

        self.right = True
        self.left = False
        
        self.spheres_list = []
    
        
    def updateHp(self, hp):
        self.hp += hp


    def change_player_sprite(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.set_sprite_path('.\game_test\sprites\player-l.png')
                self.player_sprite_load_image()

                self.right = False
                self.left = True
            
            if event.key == pygame.K_d:
                self.set_sprite_path('.\game_test\sprites\player-r.png')
                self.player_sprite_load_image()

                self.right = True
                self.left = False
            
                
    def player_sprite_load_image(self):
        self.sprite  = pygame.image.load(self.sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.size[0], self.size[1]))
    
    
    def move_player(self):
        keys = pygame.key.get_pressed()
        
        self.rect.x += (keys[pygame.K_d] - keys[pygame.K_a]) * self.veloc
        self.rect.y += (keys[pygame.K_s] - keys[pygame.K_w]) * self.veloc

        self.rect.centerx = self.rect.centerx % self.screen.surface.get_width()
        self.rect.centery = self.rect.centery % self.screen.surface.get_height()
        
        if self.rect.x < 0:
            self.rect.x = 0
        
        if self.rect.x + self.size[0] > self.screen.screen_size[0]:
            self.rect.x = self.screen.screen_size[0] - self.size[0]
        
        if self.rect.y < 0:
            self.rect.y = 0
        
        if self.rect.y + self.size[1] > self.screen.screen_size[1]:
            self.rect.y = self.screen.screen_size[1] - self.size[1]

        if self.rect.y > 704:
            self.rect.y = 704
            
    
    def throw_sphere(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                self.spheres_list.append(Sphere(self.screen, [40, 40], [self.rect.x, self.rect.y], 5, self.right))
                
        
    # FUNCAO PARA CHEGAR A VIDA ATUAL DO PLAYER      
    def check_hp(self):
        pass