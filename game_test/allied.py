import pygame

from creature import Creature

class Allied(Creature):
    def __init__(self, screen, size, location):
        super().__init__(screen, size, location, sprite_path='.\game_test\sprites\goblin_friend.png', is_active=True)