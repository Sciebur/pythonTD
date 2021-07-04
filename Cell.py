from enum import Enum
from Turret import *


class CellType(Enum):
    BAZA = 1
    SPAWNER = 2
    PATH = 3
    BUILDABLE = 4
    DEFAULT = 5


class Cell:
    type = CellType.DEFAULT
    turret = None
