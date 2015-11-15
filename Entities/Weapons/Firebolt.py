import pygame
from Entities.Weapons.RangedWeapon import RangedWeapon
from Entities.Weapons.Projectile import Projectile


class Firebolt(RangedWeapon):
    def __init__(self, weapon_x, weapon_y, direction):
        self.weapon_x = weapon_x
        self.weapon_y = weapon_y
        self.range = 32
        self.damage = 20
        self.speed = 2
        self.bullet_surface = pygame.Surface((16, 16))
        self.direction = direction
        self.bullet = Projectile(self.weapon_x, self.weapon_y, self.speed, self.direction, self.damage, pygame.image.load("graphics/sprites/entities/entity16_fireball.png").convert(), self.range)
        self.__elapsed_time = 0
        self.__previous_time = 0
        self.__update_time = 10
        # self.bullet_sprite = pygame.image.load("graphics/sprites/entities/entity16_fireball.png").convert()
        super().__init__(self.range, self.damage, self.speed)

    def __update_delta(self, d):
        # print((self.__elapsed_time, self.__previous_time, self.__update_time))
        self.__elapsed_time += d
        if self.__elapsed_time - self.__previous_time > self.__update_time:
            self.__previous_time = self.__elapsed_time
            print("hey")
            return True
        else:
            return False

    def shoot(self, delta_time):
        """
        :param x: x position of the shooter
        :param y: y position of the shooter
        :param direction: direction the projectile is being shot in
        :return:
        """

        if self.direction is "right":
            print("direction right")
            self.bullet.x += self.bullet.speed
        elif self.direction is "left":
            print("direction left")
            self.bullet.x -= self.bullet.speed
        elif self.direction is "up":
            print("direction up")
            self.bullet.y += self.bullet.speed
        else:
            print("direction down")
            self.bullet.y -= self.bullet.speed
        # if self.__update_delta(delta_time):
        #     self.bullet.x += self.bullet.speed
        #     print(self.bullet.x)
            # bullet.draw(self.bullet_surface)

        # if direction is "top":
        #     while y <= bullet.range:
        #         y += bullet.speed
        #         print("x: %d, y: %d" % x,y)
        # elif direction is "right":
        #     while x <= bullet.range:
        #         x += bullet.speed
        #         print("x: %d, y: %d" % x,y)
        # elif direction is "bottom":
        #     while y >= bullet.range:
        #         y -= bullet.speed
        #         print("x: %d, y: %d" % x,y)
        # else:
        #     while x >= bullet.range:
        #         x -= bullet.speed
        #         print("x: %d, y: %d" % x,y)
    def draw(self, screen):
        screen.blit(self.bullet.sprite, pygame.Rect(self.bullet.x,self.bullet.y,16,16))
