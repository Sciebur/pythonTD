import math

import pygame
from Cell import *
from Screen import *
from Turret import *
from Enemy import *


class GameManager:
    mapa = []
    clock = pygame.time.Clock()
    path = []
    enemies = []  # type: List[Enemy]
    base_hp = 100
    base_max_hp = 100
    mana = 100

    def create_map(self):
        for i in range(10):
            rząd = []
            for j in range(10):
                cell = Cell()
                rząd.append(cell)
            self.mapa.append(rząd)

        self._setup_map()

    def _setup_map(self):
        self.mapa[4][0].type = CellType.SPAWNER
        self.mapa[4][1].type = CellType.PATH
        self.mapa[4][2].type = CellType.PATH
        self.mapa[4][3].type = CellType.PATH
        self.mapa[5][3].type = CellType.PATH
        self.mapa[6][3].type = CellType.PATH
        self.mapa[6][4].type = CellType.PATH
        self.mapa[6][5].type = CellType.PATH
        self.mapa[6][6].type = CellType.PATH
        self.mapa[5][6].type = CellType.PATH
        self.mapa[4][6].type = CellType.PATH
        self.mapa[4][7].type = CellType.PATH
        self.mapa[4][8].type = CellType.PATH
        self.mapa[4][9].type = CellType.BAZA

    def spawn_enemy(self):
        self.enemies.append(Enemy(self.get_enemy_path()))

    def get_enemy_path(self):
        return [(40, 360), (280, 360), (280, 520), (520, 520), (520, 360), (760, 360)]

    def get_all_turrets(self):
        result = []
        for row in self.mapa:
            for cell in row:
                if cell.turret:
                    result.append(cell.turret)
        return result

    def shoot(self):
        def _distance_sq(a, b):
            return a.distance_squared_to(b)

        for turret in self.get_all_turrets():
            closest_distance_sq = 99999999
            closest_enemy = None
            for enemy in self.enemies:
                dist_sq = _distance_sq(turret.position, enemy.position)
                if dist_sq < closest_distance_sq:
                    closest_distance_sq = dist_sq
                    closest_enemy = enemy

            if closest_enemy and turret.can_shoot() and math.sqrt(closest_distance_sq) <= turret.range:
                turret.shoot()
                closest_enemy.take_dmg(turret.dmg)
                if closest_enemy.is_dead():
                    self.mana = self.mana + closest_enemy.max_hp
                    self.enemies.remove(closest_enemy)

        for enemy in self.enemies:
            if enemy.is_at_base():
                self.base_hp = self.base_hp - enemy.hp
                self.enemies.remove(enemy)

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()

    def get_base_hp_fraction(self):
        return self.base_hp / self.base_max_hp

    def build_turret(self, pos):
        turret = Turret((0, 0))
        if self.mana < turret.cost:
            print("Brakuje many")
            return

        col = math.floor(pos[0] / 80)
        row = math.floor(pos[1] / 80)

        cell = self.mapa[row][col]

        if cell.type == CellType.BUILDABLE or cell.type == CellType.DEFAULT:
            position = Vector((col + .5) * 80, (row + .5) * 80)
            turret = Turret(position)
            cell.turret = turret
            self.mana = self.mana - turret.cost
