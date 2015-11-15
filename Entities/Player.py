import pygame
from Entities.Character import Character
from Scale import *


class Player(Character):
    def __init__(self, start_pos, health):
        speed = 1
        super().__init__(start_pos, speed, 70, health, "graphics/objects/entities/entity16_player.png")

        self.frames_up = []
        self.frames_down = []
        self.frames_left = []
        self.frames_right = []

        self.image = pygame.Surface((16, 20))
        self.rect = self.image.get_rect(topleft=start_pos)
        self.load_images()
        self.sfx = self.load_sfx()

        self.anim_index = 0
        self.images = self.frames_down
        self.moving = False

        self.can_move = {"left": True, "right": True, "up": True, "down": True}
        self.prev_direction = ""
        self.current_direction = ""
        self.__mixer_free = True
        self.__sfx_enabled = False

    @staticmethod
    def load_sfx():
        sfx = {
            "walk": "sfx/walk.wav",
            "talk": "sfx/talk.wav"
        }
        return sfx

    def enable_sfx(self):
        self.__sfx_enabled = True

    def play_sfx(self, key):
        if not self.__sfx_enabled:
            return
        if key == "sfx/talk.wav" or self.__mixer_free:
            pygame.mixer.music.load(self.sfx[key])
            pygame.mixer.music.play(0)
            self.__mixer_free = False

    def mixer_free(self):
        self.__mixer_free = True

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
        self.prev_direction = self.current_direction
        sound = True
        if keys[pygame.K_a] and self.can_move["left"]:
            self.rect.x -= self.speed
            self.images = self.frames_left
            self.update_anim()
            self.current_direction = "left"
        elif keys[pygame.K_d] and self.can_move["right"]:
            self.rect.x += self.speed
            self.images = self.frames_right
            self.update_anim()
            self.current_direction = "right"
        elif keys[pygame.K_w] and self.can_move["up"]:
            self.rect.y -= self.speed
            self.images = self.frames_up
            self.update_anim()
            self.current_direction = "up"
        elif keys[pygame.K_s] and self.can_move["down"]:
            self.rect.y += self.speed
            self.images = self.frames_down
            self.update_anim()
            self.current_direction = "down"
        else:
            self.image = self.images[0]
            sound = False
        if sound:
            self.play_sfx("walk")

    # def set_movement_blocking(self):
    #     for i in self.can_move:
    #         self.can_move[i] = True
    #     self.can_move[self.prev_direction] = False
    #
    # def unblock_movement(self):
    #     for i in self.can_move:
    #         self.can_move[i] = True
    #
    def test_for_nearby_enemies(self, enemies):
        north_test_rect = pygame.Rect(self.rect.x, self.rect.y - self.speed, 16, 16)
        south_test_rect = pygame.Rect(self.rect.x, self.rect.y + self.speed, 16, 16)
        east_test_rect = pygame.Rect(self.rect.x + self.speed, self.rect.y, 16, 16)
        west_test_rect = pygame.Rect(self.rect.x - self.speed, self.rect.y, 16, 16)

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.rect.x += 10
                enemy.rect.y += 10
                self.health -= enemy.weapon.damage

    def test_for_collisions(self, walls):
        north_test_rect = pygame.Rect(self.rect.x, self.rect.y - self.speed, 16, 16)
        south_test_rect = pygame.Rect(self.rect.x, self.rect.y + self.speed, 16, 16)
        east_test_rect = pygame.Rect(self.rect.x + self.speed, self.rect.y, 16, 16)
        west_test_rect = pygame.Rect(self.rect.x - self.speed, self.rect.y, 16, 16)

        for key in self.can_move:
            self.can_move[key] = True

        for wall in walls:
            if wall.is_solid():
                if wall.is_colliding(north_test_rect):
                    self.can_move["up"] = False
                if wall.is_colliding(south_test_rect):
                    self.can_move["down"] = False
                if wall.is_colliding(east_test_rect):
                    self.can_move["right"] = False
                if wall.is_colliding(west_test_rect):
                    self.can_move["left"] = False

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

        self.time_elapsed += delta

    def draw(self, surface):
        # *4 Scaling
        bigger_img, image_rect = Scale.scale(self.image, self.rect.x, self.rect.y)
        surface.blit(bigger_img, image_rect)

        if self.health <= 0:
            self.die(surface)

    def is_colliding(self, rect):
        return self.rect.colliderect(rect)

    def die(self, surface):
        # surface.blit(pygame.i)
        pass

    def get_centre_rect(self):
        width = 16
        height = 16
        pos_x, pos_y = self.get_centre()
        return pygame.Rect(pos_x - (width/2), pos_y - (height/2), width, height)
