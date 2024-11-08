from enemy import Enemy
from creature import Creature

class Goblin(Creature, Enemy):
    def __init__(self, screen, size, location, veloc, hp):
        super().__init__(screen, size, location, sprite_path='.\game_test\sprites\goblin.png', is_active=True)
        self.veloc = veloc
        self.hp = hp
        self.tick_pos = 0
        
    
    def valid_player_hp(self, player, tick):
        if player.hp <= 0:
                player.death = True
        else:
            player.hp -= 1
            print(player.hp)
            self.tick_pos = tick
    
    
    def demage_player(self, player, tick):
        if self.tick_pos == 0 and self.rect.colliderect(player.rect):
            self.valid_player_hp(player, tick)
        
        if self.tick_pos - tick > 120 and self.rect.colliderect(player.rect):
            self.valid_player_hp(player, tick)
