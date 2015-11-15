import pygame
from Entities.Character import Character


class Player(Character):
    def __init__(self, start_pos, health):
        speed = 2
        super().__init__(start_pos, speed, 150, health, "graphics/sprites/entities/entity16_generic.png")

        self.frames_up = []
        self.frames_down = []
        self.frames_left = []
        self.frames_right = []

        self.image = pygame.Surface((19, 25))
        self.rect = self.image.get_rect(topleft=start_pos)
        self.load_images()

        self.anim_index = 0
        self.images = self.frames_down

    def load_images(self):

        for i in range(12):
            y = i*self.rect.h
            self.frames_down.append(self.sprite_sheet.get_image(0, y, self.rect.w, self.rect.h))
            self.frames_right.append(self.sprite_sheet.get_image(20, y, self.rect.w, self.rect.h))
            self.frames_left.append(self.sprite_sheet.get_image(40, y, self.rect.w, self.rect.h))
            self.frames_up.append(self.sprite_sheet.get_image(60, y, self.rect.w, self.rect.h))

    def check_keys(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.images = self.frames_left
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.images = self.frames_right
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.images = self.frames_up
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            self.images = self.frames_down

    def update(self, keys, delta):
        self.check_pos()

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
