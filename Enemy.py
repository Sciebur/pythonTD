import pygame
from pygame.surface import Surface
from enum import Enum
from typing import Tuple, List

Vector = pygame.math.Vector2


class EnemyType(Enum):
    Normal = 0,
    Fast = 1


class Enemy:

    def __init__(self, path):
        self.path = list(path)[1:]
        self.position = path[0]
        self.hp = self.max_hp
        self.atBase = False

        self.image = pygame.image.load(self.image_file).convert()
        self.image = pygame.transform.scale(self.image, (40, 40))

    def _distance_to_next_node(self):
        return Vector(self.path[0]) - Vector(self.position)

    def move(self):
        if len(self.path) == 0:
            self.atBase = True
            return

        if self._distance_to_next_node().length() < 0.1:
            self.path.pop(0)
            return

        remaining = self._distance_to_next_node()
        remaining.scale_to_length(self.speed)
        self.position = self.position + remaining

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg

    def is_dead(self):
        return self.hp <= 0

    def is_at_base(self):
        return self.atBase

    def get_image(self) -> Surface:
        return self.image


class EnemyNormal(Enemy):
    max_hp = 3
    speed = 5
    image_file = "asset/enemyNormal.bmp"


class EnemyFast(Enemy):
    max_hp = 2
    speed = 10
    image_file = "asset/enemyFast.bmp"
