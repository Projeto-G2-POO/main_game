from creature import Creature

class Goblin(Creature):
    def __init__(self, screen, size, location, veloc, hp):
        super().__init__(screen, size, location, sprite_path='.\game_test\sprites\goblin.png', is_active=True)
        self.veloc = veloc
        self.hp = hp

    def chase_player(self, player):
        if player.rect.x != self.rect.x:
            if player.rect.x > self.rect.x:
                self.rect.x += self.veloc
            else:
                self.rect.x -= self.veloc
                
        if player.rect.y != self.rect.y:
            if player.rect.y > self.rect.y:
                self.rect.y += self.veloc
            else:
                self.rect.y -= self.veloc
                
    
    def check_hp(self, enemie):
        if self.hp <= 0:
            enemie.is_active = False
        
    
    # FUNCAO PARA DAR DANO NO PLAYER    
    def demage_player(self, player):
        pass
            