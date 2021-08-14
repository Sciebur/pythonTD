import pygame
from enum import Enum

Vector = pygame.math.Vector2


class EnemyType(Enum):
    Normal = 0,
    Fast = 1


class Enemy:
    max_hp = 0
    speed = 0
    hp = 0
    path = []
    position = None
    atBase = False

    def __init__(self, path):
        self.path = list(path)[1:]
        self.position = path[0]
        self.hp = self.max_hp

    def _distance(self):
        return Vector(self.path[0]) - Vector(self.position)

    def move(self):
        if len(self.path) == 0:
            self.atBase = True
            return

        if self._distance().length() < 0.1:
            self.path.pop(0)
            return

        remaining = self._distance()
        remaining.scale_to_length(self.speed)
        self.position = self.position + remaining

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg

    def is_dead(self):
        return self.hp <= 0

    def is_at_base(self):
        return self.atBase


class EnemyNormal(Enemy):
    max_hp = 3
    speed = 5


class EnemyFast(Enemy):
    max_hp = 2
    speed = 10
