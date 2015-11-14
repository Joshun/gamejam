import pygame
from Entities.Weapons.RangedWeapon import RangedWeapon


class Firebolt(RangedWeapon):
    def __init__(self):
        self.range = 64
        self.damage = 20
        self.speed = 8
        self.bullet_sprite = pygame.image.load("graphics/sprites/entities/entity16_fireball.png").convert()
        super().__init__(self.range, self.damage, self.speed)

    def shoot(self, x, y, direction, damage, sprite, range):
        """
        :param x: x position of the shooter
        :param y: y position of the shooter
        :param direction: direction the projectile is being shot in (0: up, 1: right, 2: down, 3: left)
        :param damage: damage the weapon does
        :param sprite: image for the projectile
        :param range: range of the weapon
        :return:
        """
        bullet = Projectile(x, y, self.speed, direction, self.weapon_damage, self.bullet_sprite, self.weapon_range)

        # if direction == 0:
        #     while(y <= bullet.range):
        #         y += bullet.speed
        # elif direction == 1:
        #     while(x <= bullet.range):
        #         x += bullet.speed
        # elif direction == 2:
        #     while(y )
