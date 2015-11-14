import pygame


class Projectile():
    def __init__(self, x, y, velocity, direction, damage, bullet_sprite, bullet_range):
        self.velocity = velocity
        self.direction = direction
        self.sprite = bullet_sprite
        self.damage = damage
        self.range = bullet_range
