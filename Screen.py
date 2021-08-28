import pygame
from Cell import *
from Utils import *
from typing import List
from GameManager import *


# from Enemy import *


# TODO make it a class

class Screen:
    def __init__(self, manager: GameManager):
        self.screen = pygame.display.set_mode((800, 800))
        self.manager = manager

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_map()
        self.draw_enemies()
        self.draw_base_hp()
        self.draw_mana()

        pygame.display.update()

    def draw_map(self):
        prawo = 0
        dol = 0
        czarna = False

        for row in self.manager.map.map:
            prawo = 0

            for cell in row:
                color = self.get_cell_color(cell, czarna)
                czarna = not czarna

                pygame.draw.rect(self.screen, color, (prawo, dol, 80, 80))

                if cell.turret is not None:
                    if isinstance(cell.turret, TurretNormal):
                        color = (255, 179, 48)
                    elif isinstance(cell.turret, TurretSniper):
                        color = (5, 120, 18)
                    else:
                        raise

                    pygame.draw.circle(self.screen, color, (prawo + 40, dol + 40), 35)

                    if cell.turret.get_current_enemy():
                        pygame.draw.line(self.screen, (255, 0, 0), cell.turret.position,
                                         cell.turret.get_current_enemy().position)

                prawo = prawo + 80

            czarna = not czarna
            dol = dol + 80

    @staticmethod
    def get_cell_color(cell, czarna):
        if cell.type == CellType.BAZA:
            color = pygame.Color(127, 127, 127)
        elif cell.type == CellType.SPAWNER:
            color = pygame.Color(81, 140, 83)
        elif cell.type == CellType.PATH:
            color = pygame.Color(62, 222, 67)
        elif cell.type == CellType.BUILDABLE:
            color = pygame.Color(48, 233, 240)
        else:
            if czarna:
                color = pygame.Color('black')
            else:
                color = pygame.Color('white')

        return color

    def draw_enemies(self):
        for enemy in self.manager.enemies:

            if isinstance(enemy, EnemyNormal):
                color_back = (255, 0, 17)
                color_front = (16, 16, 17)
            elif isinstance(enemy, EnemyFast):
                color_back = (4, 57, 143)
                color_front = (32, 91, 186)
            else:
                raise

            pygame.draw.circle(self.screen, color_back, (enemy.position[0], enemy.position[1]), 20)
            pygame.draw.circle(self.screen, color_front, (enemy.position[0], enemy.position[1]),
                               20 * enemy.hp / enemy.max_hp)

    def draw_base_hp(self):
        for row in self.manager.map.map:
            for cell in row:
                if cell.type is CellType.BAZA:
                    pos = get_cell_centre(self.manager.map.map, cell)
                    hp_fraction = self.manager.get_base_hp_fraction()

                    pygame.draw.rect(self.screen, (92, 88, 88), (
                        pos[0] - 40 * hp_fraction, pos[1] - 40 * hp_fraction, 80 * hp_fraction, 80 * hp_fraction))

    def draw_mana(self):
        font = pygame.font.SysFont(pygame.font.get_default_font(), 50)
        mana = '{:d}'.format(self.manager.mana)
        text_surface = font.render(mana, False, (47, 168, 29))
        down = self.screen.get_height() - 50
        right = 50
        self.screen.blit(text_surface, (right, down))
