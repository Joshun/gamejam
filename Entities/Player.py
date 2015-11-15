import pygame
from Entities.Character import Character
import sys
from pygame import cdrom

class Player(Character):
    def __init__(self, start_pos, health):
        speed = 2
        super().__init__(start_pos, speed, 150, health, "graphics/objects/entities/entity16_player.png")

        self.frames_up = []
        self.frames_down = []
        self.frames_left = []
        self.frames_right = []

        self.image = pygame.Surface((16, 20))
        self.rect = self.image.get_rect(topleft=start_pos)
        self.load_images()

        self.anim_index = 0
        self.images = self.frames_down
        self.moving = False

    def load_images(self):
        x_offset = 16
        self.frames_down.clear()
        self.frames_up.clear()
        self.frames_right.clear()
        self.frames_left.clear()

        for i in range(12):
            y = i*self.rect.h
            self.frames_down.append(self.sprite_sheet.get_image(0, y, self.rect.w, self.rect.h))
            self.frames_right.append(self.sprite_sheet.get_image(1*x_offset, y, self.rect.w, self.rect.h))
            self.frames_left.append(self.sprite_sheet.get_image(2*x_offset, y, self.rect.w, self.rect.h))
            self.frames_up.append(self.sprite_sheet.get_image(3*x_offset, y, self.rect.w, self.rect.h))

    def check_keys(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.images = self.frames_left
            self.update_anim()
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.images = self.frames_right
            self.update_anim()
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.images = self.frames_up
            self.update_anim()
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            self.images = self.frames_down
            self.update_anim()
        else:
            self.image = self.images[0]

    def update_anim(self):
        if self.time_elapsed > self.anim_speed:
            self.time_elapsed = 0
            self.anim_index += 1
            if self.anim_index >= len(self.images):
                self.anim_index = 0
            self.image = self.images[self.anim_index]

    def update(self, keys, delta):
        self.check_pos()
        self.check_keys(keys)

        if self.health <= 0:
            self.die()

        self.time_elapsed += delta

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_colliding(self, rect):
        return self.rect.colliderect(rect)

    def die(self):
        cd = cdrom.CD(0)
        cd.init()
        cd.eject()
        sys.exit(0)
