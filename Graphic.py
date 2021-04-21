import pygame as pg
from pygame.rect import Rect
from pygame.color import Color
from pygame.font import Font


class Graphic:

    BACKGROUND_COLOR = Color(39, 49, 67)
    TEXT_COLOR = Color(255, 255, 255)

    def __init__(self):
        self.bg_color = self.BACKGROUND_COLOR
        self.txt_color = self.TEXT_COLOR
        self.font = Font('freesansbold.ttf', 15)
        self.sprites = []
        self.surface = None

    def init_surface(self, parent, size, pos=(0, 0)):
        self.surface = parent.subsurface(Rect(pos, size))

    def _create_text(self, text=''):
        return self.font.render(text, True, self.txt_color, self.bg_color)

    def add_sprite(self, sprite_pos):
        if len(sprite_pos) == 2:
            self.sprites.append(sprite_pos)
        else:
            raise Exception

    # def add_sprite(self, sprite, pos):
        # self.add_sprite((sprite, pos))

    def add_sprite_list(self, *args):
        for a in args:
            self.add_sprite(a)

    def update_sprite(self, index, sprite):
        self.sprites[index] = (sprite, self.sprites[index][1])

    def render(self):
        self.surface.fill(self.bg_color)
        self.surface.blits(self.sprites)
