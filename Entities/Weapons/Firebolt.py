import pygame
from Entities.Weapons.RangedWeapon import RangedWeapon
from Entities.Weapons.Projectile import Projectile


class Firebolt(RangedWeapon):
    def __init__(self):
        self.range = 32
        self.damage = 20
        self.speed = 8
        self.bullet_sprite = pygame.Surface((16, 16))
        # self.bullet_sprite = pygame.image.load("graphics/sprites/entities/entity16_fireball.png").convert()
        super().__init__(self.range, self.damage, self.speed)

    def shoot(self,x,y, direction):
        """
        :param x: x position of the shooter
        :param y: y position of the shooter
        :param direction: direction the projectile is being shot in
        :param damage: damage the weapon does
        :param sprite: image for the projectile
        :param range: range of the weapon
        :return:
        """
        bullet = Projectile(x,y, self.speed, direction, self.weapon_damage, pygame.image.load("graphics/sprites/entities/entity16_fireball.png").convert(), self.weapon_range)
        bullet.draw(self.bullet_sprite)
        if direction == "top":
            while y <= bullet.range:
                y += bullet.speed
                # print("x: %d, y: %d" % x,y)
        elif direction == "right":
            while x <= bullet.range:
                x += bullet.speed
                # print("x: %d, y: %d" % x,y)
        elif direction == "bottom":
            while y >= bullet.range:
                y -= bullet.speed
                # print("x: %d, y: %d" % x,y)
        else:
            while x >= bullet.range:
                x -= bullet.speed
                # print("x: %d, y: %d" % x,y)
