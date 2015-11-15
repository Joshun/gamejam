import pygame

class Inventory(object):
    def __init__(self, size = 10):
        self.items = []
        self.size = size
        self.closed = True

    def draw(self, screen):
        if not self.closed:
            bg = self.setup_background(screen.get_size())
            self.draw_bag(bg)
            self.draw_items(bg)
            screen.blit(bg, (0, 0))


    def draw_items(self, bg):
        pass

    def draw_bag(self, bg):
        pass

    def can_fit(self, item):
        return len(self.items) + item.size < self.size

    def add_item(self, item):
        if can_fit(item):
            self.items.append(item)
        else:
            raise Exception('Bag full noob')

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

