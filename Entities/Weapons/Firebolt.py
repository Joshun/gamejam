import pygame
from Entities.Weapons.RangedWeapon import RangedWeapon


class Firebolt(RangedWeapon):
    def __init__(self):
        self.range = 64
        self.damage = 20
        self.speed = 8
        self.bullet_sprite = pygame.image.load("graphics/sprites/entities/entity16_fireball.png").convert()
        super().__init__(self.range, self.damage, self.speed)

    def shoot(self, direction, sprite, damage, range):
        bullet = Projectile(self.speed, direction, self.bullet_sprite, self.weapon_damage, self.weapon_range)
