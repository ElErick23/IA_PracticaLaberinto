from Graphic import Graphic
import pygame as pg
from pygame.rect import Rect
from pygame.color import Color
from Graphic import Graphic


class Cell(Graphic):

    CODES = {
        0: {'Means': 'Wall', 'Color': Color(0, 0, 0)},
        1: {'Means': 'Road', 'Color': Color(255, 255, 255)},
        2: {'Means': 'Water', 'Color': Color(100, 150, 255)},
    }

    WIDTH, HEIGHT = 100, 100

    def __init__(self, code, parent, x, y, width=WIDTH, height=HEIGHT):
        self.pos = (x * width, y * height)
        super().__init__(parent, self.pos, (width, height))
        self.code = code
        self.x = x
        self.y = y
        self.selected = False

    def __update_color(self):
        self.bg_color = self.CODES[self.code]['Color']

    def is_selected(self, pos):
        x, y = self.surface.get_abs_offset()
        r = self.surface.get_rect(x=x, y=y)
        self.selected = r.collidepoint(pos)
        return self.selected

    def is_path(self):
        return self.code != 0

    def render(self, player_sprite=None):
        self.__update_color()
        super().render()
        if player_sprite:
            self.surface.blit(player_sprite, (0, 0))
        if self.selected:
            pg.draw.rect(self.surface, Color(255, 0, 0, 0),
                         self.surface.get_rect(), width=5)

    # def get_coords(self):
    #     return '({}, {})'.format(chr(self.x + 65), self.y + 1)

    # def get_mean(self):
    #     return self.CODES[self.code]['Means']

    def __repr__(self):
        coords = '({}, {})'.format(chr(self.x + 65), self.y + 1)
        means = self.CODES[self.code]['Means']
        return '{} {}: {}'.format(coords, means, str(self.code))
