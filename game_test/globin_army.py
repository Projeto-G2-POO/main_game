from goblin import Goblin

class Goblin_Army(Goblin):
    def __init__(self, screen, size, location, veloc, hp):
        super().__init__(screen, size, location, veloc, hp)
        
    
    # TEM Q DAR MAIS DANO Q O GOBLIN NORMAL (2 DE DANO)
    def demage_player(self, player):
        pass