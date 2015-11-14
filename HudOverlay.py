import pygame

class HudOverlay():
    def __init__(self, player):
        self.player = player
        self.heart_size = (50,50)

    def draw(self, screen):
        background = self.setup_background((screen.get_size()[0],30))
        self.draw_hearts(background, self.player.health // 33)
        screen.blit(background, (0,0))

    def update(self, keys):
        if keys[pygame.K_h]:
            self.player.hit(10)

    def draw_hearts(self, bg, heart_count):
        offset = 0
        for i in range(heart_count):
            self.draw_heart(bg, offset)
            offset += self.heart_size[0]+10

    def draw_heart(self, bg, offset):
        background = pygame.Surface(self.heart_size,50)
        background = background.convert()
        background.fill((247, 0, 190, 50))
        bg.blit(background, (offset,0))

    def setup_background(self, size):
        background = pygame.Surface(size,50)
        background = background.convert()
        background.fill((250, 250, 250, 50))
        return background



        