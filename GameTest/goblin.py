import pygame
from creature import Creature

class Goblin(Creature):
    def __init__(self, size, location, veloc, hp):
        super().__init__(size, location, sprite_path='.\GameTest\sprites\goblin_sprite.png')
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