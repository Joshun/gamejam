from Entities.Character import Character
from SpriteSheet import SpriteSheet
import pygame


class NPC(Character):
    def __init__(self, start_pos):
        speed = 2
        super().__init__(start_pos, speed, 70, 0, "graphics/sprites/entities/entity16_generic.png")

        self.frames_down = []

        self.image = pygame.Surface((20, 25))
        self.rect = self.image.get_rect(topleft=start_pos)
        self.load_images()

        self.anim_index = 0
        self.images = self.frames_down

    def load_images(self):

        for i in range(12):
            y = i*self.rect.h
            self.frames_down.append(self.sprite_sheet.get_image(60, y, self.rect.w, self.rect.h))

    def update(self, delta):
        self.time_elapsed += delta

        if self.time_elapsed > self.anim_speed:
            self.time_elapsed = 0
            self.anim_index += 1
            if self.anim_index >= len(self.images):
                self.anim_index = 0
            self.image = self.images[self.anim_index]

    def draw(self, surface):
        surface.blit(self.image, self.rect)