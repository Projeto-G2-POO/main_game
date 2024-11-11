from color import Color

class Level():
    def __init__(self, number, enemies, veloc, player, enemies_list = []):
        self.number = number
        self.enemies = enemies
        self.veloc = veloc
        
        self.player= player
        self.enemies_list = enemies_list
        
        self.enemies_spawned = 0


    def home_power(self, goblin, dialogue_box):
        self.player.enemies_deaths = 0
        self.enemies_spawned = 0
        self.player.hp = 5
        
        self.number += 1
        self.enemies += 5
        self.veloc += 1
        
        self.enemies_list.clear()
        
        if self.number % 4 == 0:
            self.veloc = 2
            self.enemies = 5
        
        goblin.is_active = True
        
        new_text_dialogue = f'Uau, você se saiu muito bem! Vamos para o level {self.number}?'
        dialogue_box.set_text(new_text_dialogue, Color.white())
                     
                
    def power_enemy(self, dialogue_box, screen, ticks, goblin, enemy_type):
        if dialogue_box.level_active:
            goblin.is_active = False
            
            if ticks % 50 == 0 and self.enemies_spawned <= self.enemies:
                screen.create_enemy(self.enemies_list, self.veloc, enemy_type)
                self.enemies_spawned += 1
            
            if ticks % 50 == 0 and self.player.enemies_deaths >= self.enemies:
                dialogue_box.level_active = False
                self.home_power(goblin, dialogue_box) 