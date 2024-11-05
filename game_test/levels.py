from color import Color

class Level():
    def __init__(self, number, enemies, veloc, enemies_list = [], all_enemies_list = []):
        self.number = number
        self.enemies = enemies
        self.veloc = veloc
        
        self.enemies_list = enemies_list
        self.all_enemies_list = all_enemies_list


    def home_power(self, goblin, dialogue_box):
        self.number += 1
        self.enemies += 5
        self.veloc += 1
        
        goblin.is_active = True
        
        new_text_dialogue = f'Uau, você se saiu muito bem!\n Vamos para o level {self.number}?'
        dialogue_box.set_text(new_text_dialogue, Color.white())
        

    def power_goblin(self, dialogue_box, screen, ticks, goblin):
        if dialogue_box.level_active:
            goblin.is_active = False
            
            if ticks % 50 == 0 and len(self.all_enemies_list) < self.enemies:
                screen.create_goblin(self.enemies_list, self.all_enemies_list, self.veloc)
            
            if ticks % 50 == 0 and len(self.enemies_list) <= 0:
                dialogue_box.level_active = False
                self.home_power(goblin, dialogue_box)
                
                
    def power_goblin_fort(self, dialogue_box, screen, ticks, goblin):
        if dialogue_box.level_active:
            goblin.is_active = False
            
            if ticks % 50 == 0 and len(self.all_enemies_list) < self.enemies:
                screen.create_goblin(self.enemies_list, self.all_enemies_list, self.veloc)
            
            if ticks % 50 == 0 and len(self.enemies_list) <= 0:
                dialogue_box.level_active = False
                self.home_power(goblin, dialogue_box)
                