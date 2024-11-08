from creature import Creature

class Sphere(Creature):
    def __init__(self, screen, size, location, veloc, right):
        super().__init__(screen, size, location, sprite_path='.\game_test\sprites\sphere.png', is_active=True)
        self.veloc= veloc
        self.right = right
        
        
    def move_sphere(self, spheres, sphere):
        if self.rect.x < 0 or self.rect.x > 800:
            spheres.pop(spheres.index(sphere))
        elif self.right:
            self.rect.x += self.veloc
        else:
            self.rect.x -= self.veloc


    def colide_with_enemies(self, enemies, player):
        for enemie in enemies:
            if self.rect.colliderect(enemie):
                enemie.hp -= 1
                if enemie.hp <= 0:
                    enemies.pop(enemies.index(enemie))
                    player.enemies_deaths += 1