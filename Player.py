import pygame as pg
from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN
from pygame.constants import KEYDOWN
from Cell import Cell
from Handler import Handler


class Player:

    def __init__(self, start, sense_cell):
        self.x, self.y = start
        self.sprite = None
        self.discovered_cells = []
        self.sense_cell = sense_cell
        Handler().set_callback(KEYDOWN, self.move)

    def load_sprite(self, size):
        img = pg.image.load("resources/player.png").convert_alpha()
        self.sprite = pg.transform.scale(img, size)

    def is_at(self, x, y):
        return (self.x, self.y) == (x, y)

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

    def moveUp(self):
        self.y -= 1

    def moveDown(self):
        self.y += 1

    def move(self, event):
        x_dest, y_dest = self.x, self.y
        if event.key == K_DOWN:
            y_dest += 1
        elif event.key == K_UP:
            y_dest -= 1
        elif event.key == K_LEFT:
            x_dest -= 1
        elif event.key == K_RIGHT:
            x_dest += 1

        if not self.is_at(x_dest, y_dest):
            dest_cell = self.sense_cell(x_dest, y_dest)
            if dest_cell != None and dest_cell.is_path():
                self.x, self.y = x_dest, y_dest
