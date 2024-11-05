class Level():
    def __init__(self, number, enemies, veloc, enemies_list = [], all_enemies_list = []):
        self.number = number
        self.enemies = enemies
        self.veloc = veloc
        
        self.enemies_list = enemies_list
        self.all_enemies_list = all_enemies_list

    def home_power(self, goblin):
        self.number += 1
        goblin.is_active = True
        
        
        

    def power1(self, dialogue_box, screen, ticks, goblin):
        if dialogue_box.level_active:
            goblin.is_active = False
            
            if ticks % 50 == 0 and len(self.all_enemies_list) <= self.enemies:
                print(len(self.all_enemies_list))
                screen.create_goblin(self.enemies_list, self.all_enemies_list, self.veloc)
            
            if ticks % 50 == 0 and len(self.enemies_list) <= 0:
                dialogue_box.level_active = False
                self.home_power(goblin)
                