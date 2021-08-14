import pygame
from enum import Enum

Vector = pygame.math.Vector2


class TurretType(Enum):
    Normal = 0,
    Sniper = 1


class Turret:
    dmg = 0
    attack_speed = 0
    range = 0
    cost = 0
    position = None
    last_attack_time = 0
    current_enemy = None

    def __init__(self, position):
        self.position = position

    def can_shoot(self):
        elapsed = pygame.time.get_ticks() - self.last_attack_time
        cooldown = 1000 / self.attack_speed
        return elapsed > cooldown

    def shoot(self):
        self.last_attack_time = pygame.time.get_ticks()

    def set_current_enemy(self, enemy):
        self.current_enemy = enemy

    def get_current_enemy(self):
        return self.current_enemy

    def set_position(self, position):
        self.position = position


class TurretNormal(Turret):
    dmg = 1
    attack_speed = 2
    range = 200
    cost = 50


class TurretSniper(Turret):
    dmg = 3
    attack_speed = 1
    range = 350
    cost = 100
