from Entities.Weapons.Weapon import Weapon
from Entities.Weapons.Projectile import Projectile

class RangedWeapon(Weapon):
    def __init__(self, weapon_range, weapon_damage, bullet_speed):
        self.weapon_range = weapon_range
        self.weapon_damage = weapon_damage
        self.speed = bullet_speed
