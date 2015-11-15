import pygame


class Inventory(object):
    def __init__(self):
        self.items = []
        self.closed = True

    def draw(self, screen):
        if not self.closed:
            bg = self.setup_background(screen.get_size())
            screen.blit(bg, (0, 0))

    def draw_items(self, bg):
        pass

    def draw_bag(self, bg):
        pass

    def setup_background(self, size):
        background = pygame.Surface(size,50)
        background = background.convert()
        background.fill((250, 0, 0, 50))
        return background

    def open(self):
        self.closed = False

    def close(self):
        self.closed = True

    def update(self):
        pass

