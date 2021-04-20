import pygame as pg
from pygame.color import Color
from Graphic import Graphic
from Maze import Maze
from pygame.rect import Rect

class Board(Graphic):

    def __init__(self, parent, pos, size):
        super().__init__(parent, pos, size)
        self.bg_color = Color(255, 150, 150)
        self.maze = Maze('resources/maze.txt', self.surface, (25, 25), (800, 800))

    def render(self):
        super().render()
        # pg.draw.rect(self.surface, self.bg_color, Rect((0, 0), (800, 25)))
        self.maze.render()