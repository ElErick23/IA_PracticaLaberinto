import pygame as pg
from pygame.color import Color
from Graphic import Graphic
from Maze import Maze
from pygame.rect import Rect

class Board(Graphic):

    def __init__(self, codes):
        super().__init__()
        self.bg_color = Color(63, 83, 120)
        self.maze = Maze(codes)

    def init_surface(self, parent, size, pos=(0, 0)):
        super().init_surface(parent, size, pos)
        maze_size = (size[0] - 25, size[1] - 25)
        final_w, final_h = self.maze.init_surface(self.surface, maze_size, (25, 25))
        return final_w + 25, final_h + 25

    def render(self):
        super().render()
        # pg.draw.rect(self.surface, self.bg_color, Rect((0, 0), (800, 25)))
        self.maze.render()