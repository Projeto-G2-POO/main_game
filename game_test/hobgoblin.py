from enemy import Enemy
from creature import Creature

class Hobgoblin(Creature, Enemy):
    def __init__(self, screen, size, location, veloc, hp):
        super().__init__(screen, size, location, sprite_path='.\game_test\sprites\hobgoblin.png', is_active=True)
        self.veloc = veloc
        self.hp = hp
        
        
    def demage_player(self, player):
        if self.rect.colliderect(player):
            if player.hp <= 0:
                player.check_hp()
            else:
                player.hp.number -= 2