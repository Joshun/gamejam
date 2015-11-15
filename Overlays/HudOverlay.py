import pygame

import pygame
from SpriteSheet import SpriteSheet
class HudOverlay:
    def __init__(self, player):
        self.player = player
        self.heart_size = (20, 20)

        self.img = pygame.image.load('graphics/objects/entities/life_heart.png')

    def draw(self, screen):
        background = self.setup_background((screen.get_size()[0], 30))
        self.draw_hearts(background, self.player.health // 33)
        screen.blit(background, (0,0))

    def update(self, keys):
        if keys[pygame.K_h]:
            self.player.hit(10)

    def draw_hearts(self, bg, heart_count):
        offset = 0
        for i in range(heart_count):
            self.draw_heart(bg, offset)
            offset += self.heart_size[0]

    def draw_heart(self, bg, offset):
        # background = pygame.Surface(self.heart_size, 50)
        # background = background.convert()
        # background.fill((247, 0, 190, 50))
        bg.blit(self.img, (offset,0))

    def setup_background(self, size):
        background = pygame.Surface(size,50)
        background = background.convert()
        return background
