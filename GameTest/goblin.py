from creature import Creature

class Goblin(Creature):
    def __init__(self, screen, size, location, veloc, hp):
        super().__init__(screen, size, location, sprite_path='.\GameTest\sprites\goblin.png', is_active=True)
        self.veloc = veloc
        self.hp = hp

    def chase_player(self, player, goblin):
        if player.x != goblin.x:
            if player.x > goblin.x:
                goblin.x += self.veloc
            else:
                goblin.x -= self.veloc
                
        if player.y != goblin.y:
            if player.y > goblin.y:
                goblin.y += self.veloc
            else:
                goblin.y -= self.veloc