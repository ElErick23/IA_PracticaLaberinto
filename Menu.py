import pygame as pg
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
from pygame.color import Color
from Handler import Handler
from Graphic import Graphic


class Menu(Graphic):

    TXT_COLOR = Color(255, 255, 255)

    def __init__(self, maze, parent, pos, size):
        super().__init__(parent, pos, size)
        self.maze = maze
        # self.pencil = pg.transform.scale(pg.image.load(
            # "resources/pencil.png").convert_alpha(), (100, 100))
        self.add_sprite_list(
            (self._create_text(), (0, 0))
            # (self.pencil, (200, 0))
        )
        Handler().set_callback_list([
            (MOUSEBUTTONDOWN, self.check_clicks),
            (MOUSEMOTION, self.update_ui)
        ])

    def update_ui(self, event):
        cell = self.maze.selected
        if cell:
            text = self._create_text(str(cell))
            self.update_sprite(0, text)

    def check_clicks(self, event):
        if event.button == 1:
            print("Click, aún no hace nada jaja")