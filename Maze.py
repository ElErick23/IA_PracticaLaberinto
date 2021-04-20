from Graphic import Graphic
import os
import sys
import pygame as pg
from pygame.constants import MOUSEMOTION
from pygame.rect import Rect
from Cell import Cell
from Player import Player
from Handler import Handler
from Graphic import Graphic


class Maze(Graphic):

    def __init__(self, filename, parent, pos, size):
        super().__init__(parent, pos, size)
        self.player = Player((0, 0), self.get_cell_at)
        self.selected = None
        self.cells = []
        with open(os.path.join(sys.path[0], filename)) as file:
            lines = file.readlines()
            for y, line in enumerate(lines):
                line = line.replace('\n', '').split(',')
                row = []
                for x, code in enumerate(line):
                    row.append(Cell(int(code), self.surface, x, y))
                self.cells.append(row)
        Handler().set_callback(MOUSEMOTION, self.check_selected)

    def check_selected(self, event):
        selections = [
            c for r in self.cells for c in r if c.is_selected(event.pos)
        ]
        self.selected = selections[0] if len(selections) else None

    def get_cell_at(self, x, y):
        if 0 <= y < len(self.cells) and 0 <= x < len(self.cells[y]):
            return self.cells[y][x]

    def render(self):
        super().render()
        for row in self.cells:
            for cell in row:
                if self.player.is_at(cell.x, cell.y):
                    cell.render(self.player.sprite)
                else:
                    cell.render()
