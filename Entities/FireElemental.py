import pygame
from Entities.Enemy import Enemy


class FireElemental(Enemy):
    def __init__(self, start_pos, move_speed, health, weapon):
        anim_speed = 150
        super().__init__(start_pos, move_speed, anim_speed, health, weapon,
                         "graphics/entities/entity16_fire.png")

        self.frames_down = []

        self.image = pygame.Surface((20, 26))
        self.rect = self.image.get_rect(topleft=start_pos)
        self.load_images()

        self.anim_index = 0
        self.images = self.frames_down

    def load_images(self):
        x_offset = 1
        y_offset = 1

        for i in range(4):
            x = i*(x_offset + self.rect.w)
            self.frames_down.append(self.sprite_sheet.get_image(x, y_offset, self.rect.w, self.rect.h))

    def update_pos(self, player):
        x_diff = self.rect.x - (player.rect.x + self.weapon.range)
        y_diff = self.rect.y - (player.rect.y + self.weapon.range)

        scale = 1
        if abs(x_diff) > abs(y_diff):
            if x_diff > 0:
                scale = -1

            self.rect.x += self.speed * scale
        else:
            if y_diff > 0:
                scale = -1

            self.rect.y += self.speed * scale

    def update(self, delta, player):
        self.time_elapsed += delta

        self.update_pos(player)

        if self.time_elapsed > self.anim_speed:
            self.time_elapsed = 0
            self.anim_index += 1
            if self.anim_index >= len(self.images):
                self.anim_index = 0
            self.image = self.images[self.anim_index]

    def draw(self, surface):
        surface.blit(self.image, self.rect)
