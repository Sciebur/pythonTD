from typing import List
from Cell import Cell
from pygame import Vector2 as Vector


def get_cell_centre(mapa: List[List[Cell]], cell: Cell):
    for map_row in mapa:
        for map_cell in map_row:
            if map_cell is cell:
                row = map_row.index(map_cell)
                col = mapa.index(map_row)
                return Vector((row + .5) * 80, (col + .5) * 80)
