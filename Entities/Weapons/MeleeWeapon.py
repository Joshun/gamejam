from Entities.Weapons.Weapon import Weapon


class MeleeWeapon(Weapon):
    def __init__(self, weapon_range, weapon_damage):
        self.weapon_range = weapon_range
        self.weapon_damage = weapon_damage
        
