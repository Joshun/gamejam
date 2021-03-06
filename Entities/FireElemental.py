import pygame
from Entities.Enemy import Enemy
from Entities.Weapons.Firebolt import Firebolt
from Scale import *


class FireElemental(Enemy):
    def __init__(self, start_pos, move_speed, health, direction):
        anim_speed = 130
        weapon = Firebolt(start_pos[0], start_pos[1], direction)
        super().__init__(start_pos, move_speed, anim_speed, health, direction, weapon,
                         "graphics/objects/entities/entity16_elemental.png")

        self.frames_up = []
        self.frames_down = []
        self.frames_left = []
        self.frames_right = []

        self.image = pygame.Surface((16, 24))
        self.rect = self.image.get_rect(topleft=start_pos)
        self.load_images()

        self.anim_index = 0
        self.images = self.frames_down

    def load_images(self):
        self.frames_down.clear()
        self.frames_up.clear()
        self.frames_right.clear()
        self.frames_left.clear()

        for i in range(12):
            y = i*self.rect.h
            x_offset = 16
            self.frames_down.append(self.sprite_sheet.get_image(0, y, self.rect.w, self.rect.h))
            self.frames_right.append(self.sprite_sheet.get_image(1*x_offset, y, self.rect.w, self.rect.h))
            self.frames_left.append(self.sprite_sheet.get_image(2*x_offset, y, self.rect.w, self.rect.h))
            self.frames_up.append(self.sprite_sheet.get_image(3*x_offset, y, self.rect.w, self.rect.h))

    def update_anim(self):
        if self.time_elapsed > self.anim_speed:
            self.time_elapsed = 0
            self.anim_index += 1
            if self.anim_index >= len(self.images):
                self.anim_index = 0
            self.image = self.images[self.anim_index]

    def update(self, delta, player):
        self.time_elapsed += delta
        self.update_pos(player, delta)
        self.weapon.shoot(delta)
        #
        # north_test_rect = pygame.Rect(self.rect.x, self.rect.y - self.speed, 16, 16)
        # south_test_rect = pygame.Rect(self.rect.x, self.rect.y + self.speed, 16, 16)
        # east_test_rect = pygame.Rect(self.rect.x + self.speed, self.rect.y, 16, 16)
        # west_test_rect = pygame.Rect(self.rect.x - self.speed, self.rect.y, 16, 16)
        #
        #
        # no_north = False
        # no_south = False
        # no_east = False
        # no_west = False
        #
        # if north_test_rect.colliderect(player.rect):
        #     no_north = True
        # if south_test_rect.colliderect(player.rect):
        #     no_south = True
        # if east_test_rect.colliderect(player.rect):
        #     no_east = True
        # if west_test_rect.colliderect(player.rect):
        #     no_west = True
        #
        # if no_north:
        #     if self.direction == "up":
        #         self.direction = "down"
        #         self.rect.y -= 32
        # elif no_south:
        #     if self.direction == "down":
        #         self.direction = "up"
        #         self.rect.y += 32
        # elif no_east:
        #     if self.direction == "right":
        #         self.direction = "left"
        #         self.rect.x -= 32
        # elif no_west:
        #     if self.direction == "left":
        #         self.direction = "right"
        #         self.rect.x += 32


        if self.direction == "up":
            self.images = self.frames_up
            self.update_anim()
        elif self.direction == "down":
            self.images = self.frames_down
            self.update_anim()
        elif self.direction == "left":
            self.images = self.frames_left
            self.update_anim()
        elif self.direction == "right":
            self.images = self.frames_right
            self.update_anim()
        else:
            self.image = self.images[0]

    def draw(self, surface):
        bigger_img, image_rect = Scale.scale(self.image, self.rect.x, self.rect.y)

        surface.blit(bigger_img, image_rect)
        self.weapon.draw(surface)
