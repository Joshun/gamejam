import pygame

import pygame
from SpriteSheet import SpriteSheet
class HudOverlay:
    def __init__(self, player):
        self.player = player
        self.heart_size = (20, 20)
        self.img = pygame.image.load('graphics/objects/entities/life_heart.png')

    def draw(self, screen):
        background = self.draw_background((screen.get_size()[0], 20), screen)
        self.draw_hearts(background, self.player.health // 20)

        screen.blit(background, (0, screen.get_size()[1]-20))

    def update(self):
        pass

    def draw_hearts(self, bg, heart_count):
        offset = 0
        for i in range(heart_count):
            self.draw_heart(bg, offset)
            offset += self.heart_size[0]

    def draw_heart(self, bg, offset):
        bg.blit(self.img, (offset, 0))

    def draw_background(self, size, screen):
        background = pygame.Surface(size, screen.get_size()[1])
        background = background.convert()
        return background
