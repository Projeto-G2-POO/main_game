from enemy import Enemy
from creature import Creature

class Goblin(Creature, Enemy):
    def __init__(self, screen, size, location, veloc, hp):
        super().__init__(screen, size, location, sprite_path='.\game_test\sprites\goblin.png', is_active=True)
        self.veloc = veloc
        self.hp = hp