import pygame


class Projectile():
    def __init__(self, velocity, direction, damage, bullet_sprite):
        self.velocity = velocity
        self.direction = direction
        self.sprite = bullet_sprite
        self.damage = damage
