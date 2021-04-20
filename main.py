import pygame as pg
from pygame.constants import HWSURFACE, RESIZABLE
from pygame import display
from Board import Board
from Handler import Handler
from pygame import QUIT
from Board import Board
from Menu import Menu
from Handler import Handler


class main:

    def __init__(self):
        pg.init()
        display.set_caption('Maze test')
        screen = display.set_mode((825, 925), HWSURFACE)
        self.handler = Handler()
        self.board = Board(screen, (0, 100), (825, 825))
        self.menu = Menu(self.board.maze, screen, (0, 0), (825, 100))
        self.running = True

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
