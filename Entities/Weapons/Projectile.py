import pygame
from Scale import *


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction, damage, bullet_sprite, bullet_range):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.sprite = bullet_sprite
        self.damage = damage
        self.range = bullet_range
        self.rect = self.sprite.get_rect(topleft=(x,y))

    def draw(self, surface):
        bigger_img, image_rect = Scale.scale(self.sprite, self.rect.x, self.rect.y)
        surface.blit(bigger_img, image_rect)
