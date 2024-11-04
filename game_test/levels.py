class Level():
    def __init__(self, number, enemies, veloc):
        self.number = number
        self.enemies = enemies
        self.veloc = veloc


    def power1(self, dialogue_box, screen, list_enemies, ticks, goblin):
        if dialogue_box.level_active:
            goblin.is_active = False
            
            if ticks % 50 == 0 and len(list_enemies) < self.enemies:
                screen.create_goblin(list_enemies, self.veloc)
            
            if len(list_enemies) > self.enemies:
                dialogue_box.level_active = False