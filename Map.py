from Cell import *


class Map:

    def __init__(self, row, cols):
        self.map = []

        for i in range(row):
            row = []
            for j in range(cols):
                cell = Cell()
                row.append(cell)
            self.map.append(row)

        self._setup_map_TEMP()

    def for_each_cell(func):
        def _decorator(self):
            for row in self.map:
                for cell in row:
                    func(cell)
        return _decorator

    def _setup_map_TEMP(self):
        self.map[4][0].type = CellType.SPAWNER
        self.map[4][1].type = CellType.PATH
        self.map[4][2].type = CellType.PATH
        self.map[4][3].type = CellType.PATH
        self.map[5][3].type = CellType.PATH
        self.map[6][3].type = CellType.PATH
        self.map[6][4].type = CellType.PATH
        self.map[6][5].type = CellType.PATH
        self.map[6][6].type = CellType.PATH
        self.map[5][6].type = CellType.PATH
        self.map[4][6].type = CellType.PATH
        self.map[4][7].type = CellType.PATH
        self.map[4][8].type = CellType.PATH
        self.map[4][9].type = CellType.BAZA


    def get_all_turrets(self):
        return [cell.turret for row in self.map for cell in row if cell.turret]

    def get_cell(self, row, col):
        return self.map[row][col]
