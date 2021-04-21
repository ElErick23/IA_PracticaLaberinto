import pygame as pg
import os
import sys
from pygame.constants import HWSURFACE, RESIZABLE
from pygame import QUIT, display
from Board import Board
from Cell import Cell
from Menu import Menu
from Handler import Handler


class main:

    def __init__(self):
        pg.init()
        with open(os.path.join(sys.path[0], 'resources/maze.txt')) as file:
            def moya(line):
                return line.replace('\n', '').split(',')
            codes = [[int(c) for c in moya(line)] for line in file.readlines()]

        if all(len(row) == len(codes[0]) for row in codes):
            ui = int(Cell.WIDTH / 4)
            board_w = Cell.WIDTH * len(codes[0]) + ui
            board_h = Cell.HEIGHT * len(codes) + ui
            menu_w = board_w
            menu_h = 50
            display.set_caption('Maze test')
            screen = display.set_mode((board_w, board_h + menu_h), HWSURFACE)
            self.handler = Handler()
            self.board = Board(screen, (0, menu_h), (board_w, board_h), ui)
            self.menu = Menu(self.board.maze, screen, (0, 0), (menu_w, menu_h))
            self.running = True
        else:
            raise Exception(
                "Error al obtener datos, las filas deben ser igual de largas")

    def on_render(self):
        self.menu.render()
        self.board.render()
        display.flip()

    def on_event(self, event):
        self.handler.exec_callbacks(event)
        if event.type == QUIT:
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
