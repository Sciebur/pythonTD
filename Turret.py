import pygame

Vector = pygame.math.Vector2


class Turret:
    dmg = 1
    attack_speed = 2
    range = 200
    cost = 50
    position = None
    last_attack_time = 0


    def __init__(self, position):
        self.position = position

    def can_shoot(self):
        elapsed = pygame.time.get_ticks() - self.last_attack_time
        cooldown = 1000 / self.attack_speed
        return elapsed > cooldown

    def shoot(self):
        self.last_attack_time = pygame.time.get_ticks()
