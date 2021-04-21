import pygame as pg
import os
import sys
from pygame.constants import HWSURFACE, RESIZABLE
from pygame import VIDEORESIZE, QUIT, display
from Board import Board
from Cell import Cell
from Menu import Menu
from Handler import Handler


class main:

    MIN_WIDTH, MIN_HEIGHT = 300, 300

    def __init__(self):
        pg.init()
        with open(os.path.join(sys.path[0], 'resources/maze.txt')) as file:
            def split(line):
                return line.replace('\n', '').split(',')
            codes = [[int(c) for c in split(line)]
                     for line in file.readlines()]

        if all(len(row) == len(codes[0]) for row in codes):
            display.set_caption('Maze test')
            self.handler = Handler()
            self.board = Board(codes)
            self.menu = Menu(self.board.maze)
            self.running = True
            self.load_screen(600, 600)
        else:
            raise Exception(
                "Error al obtener datos, las filas deben ser igual de largas")

    def load_screen(self, width, height):
        width = max(width, self.MIN_WIDTH)
        height = max(height, self.MIN_HEIGHT)
        screen = display.set_mode((width, height), HWSURFACE | RESIZABLE)
        menu_h = 50
        board_w, board_h = self.board.init_surface(screen, (width, height - menu_h), (0, menu_h))
        self.menu.init_surface(screen, (width, menu_h))
        fixed_size = (board_w, board_h + menu_h)
        if fixed_size != (width, height):
            self.load_screen(board_w, board_h + menu_h)

    def on_render(self):
        self.menu.render()
        self.board.render()
        display.flip()

    def on_event(self, event):
        self.handler.exec_callbacks(event)
        if event.type == VIDEORESIZE:
            self.load_screen(event.w, event.h)
        elif event.type == QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_cleanup(self):
        pg.quit()

    def run(self):
        while(self.running):
            pg.event.pump()
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    main().run()
