import math
from typing import List

import pygame
from Cell import *
from Screen import *
from Turret import *
from GameManager import *

Vector = pygame.math.Vector2


def main():
    pygame.init()
    pygame.display.set_caption("TowerDefense")

    manager = GameManager()
    manager.create_map()

    screen = Screen(manager)

    while True:
        manager.clock.tick(60)

        manager.move_enemies()
        manager.shoot()

        screen.draw()

        process_events(manager)


def process_events(manager):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit(0)
            if event.key == pygame.K_e:
                manager.spawn_enemy(EnemyType.Normal)
            if event.key == pygame.K_r:
                manager.spawn_enemy(EnemyType.Fast)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                manager.build_turret(pygame.mouse.get_pos(), TurretType.Normal)
            if pygame.mouse.get_pressed(3)[2]:
                manager.build_turret(pygame.mouse.get_pos(), TurretType.Sniper)


if __name__ == '__main__':
    main()
