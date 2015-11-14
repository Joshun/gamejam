import pygame
from Entities.Character import Character


class Player(Character):
    def __init__(self, start_pos, health):
        speed = 2
        super().__init__(start_pos, speed, 150, health, "graphics/sprites/entities/entity16_fire.png")

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

    def check_keys(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed
        elif keys[pygame.K_s]:
            self.rect.y += self.speed

    def update(self, keys, delta):
        self.time_elapsed += delta

        if self.time_elapsed > self.anim_speed:
            self.time_elapsed = 0
            self.anim_index += 1
            if self.anim_index >= len(self.images):
                self.anim_index = 0
            self.image = self.images[self.anim_index]
        self.check_keys(keys)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
