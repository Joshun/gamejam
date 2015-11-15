import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, direction, damage, bullet_sprite, bullet_range):
        self.velocity = velocity
        self.direction = direction
        self.sprite = bullet_sprite
        self.damage = damage
        self.range = bullet_range
        self.rect = self.sprite.get_rect(topleft=(x,y))

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)
