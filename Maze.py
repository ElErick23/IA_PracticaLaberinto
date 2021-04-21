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

    def __init__(self, codes):
        super().__init__()
        self.player = Player((0, 0), self.get_cell_at)
        self.selected = None
        self.cells = [
            [Cell(c, x, y) for x, c in enumerate(row)] for y, row in enumerate(codes)
        ]
        Handler().set_callback(MOUSEMOTION, self.check_selected)

    def init_surface(self, parent, size, pos=(0, 0)):
        super().init_surface(parent, size, pos)
        cell_w = int(size[0] / len(self.cells[0]))
        cell_h = int(size[1] / len(self.cells))
        side = min(cell_w, cell_h)
        self.player.load_sprite((side, side))
        for row in self.cells:
            for c in row:
                c.init_surface(
                    self.surface,
                    (side, side),
                    (c.x * side, c.y * side)
                )
        return side * len(self.cells[0]), side * len(self.cells)

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
