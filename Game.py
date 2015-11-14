import pygame as pg
import sys


class Game(object):

    def __init__(self):
        """Initalize the display and prepare game objects."""
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.keys = pg.key.get_pressed()
        self.done = False
        self.viewport = self.screen.get_rect()
        self.level = pg.Surface((1000, 1000)).convert()
        self.level_rect = self.level.get_rect()

    def update_viewport(self):
        """
        The viewport will stay centered on the player unless the player
        approaches the edge of the map.
        """
        self.viewport.clamp_ip(self.level_rect)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True

    def update(self):
        """Update the player and current viewport."""
        self.keys = pg.key.get_pressed()
        self.update_viewport()

    def draw(self):
        """
        Draw all necessary objects to the level surface, and then draw
        the viewport section of the level to the display surface.
        """
        self.level.fill(pg.Color("lightblue"))
        self.screen.blit(self.level, (0, 0), self.viewport)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()p
            pg.display.update()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("Game")
    pg.display.set_mode((800, 400))

    game = Game()
    game.main_loop()

    pg.quit()
    sys.exit()
