from Entities.FireElemental import *
from Entities.NPC import *

from Steve import AwfulErrorHandling


class CharacterLoader:

    def __create_enemy(self, pos, speed, enemy_type, health):
        if enemy_type == "fire_elemental":
            return FireElemental(pos, speed, health)
        else:
            AwfulErrorHandling.throw_error("Invalid enemy", enemy_type)

    def __init__(self, character_tiles):
        self.__characters = []
        for character_obj in character_tiles:
            x = character_obj.x
            y = character_obj.y
            pos = (x,y)
            properties = character_obj.properties
            speed = int(properties["speed"])
            character_type = properties["character"]
            health = int(properties["health"])
            direction = properties["direction"]

            if character_type == "enemy":
                self.__characters.append(self.__create_enemy(pos, speed, properties["enemy_type"], health))
            elif character_type == "npc":
                self.__characters.append(NPC(pos))
            else:
                AwfulErrorHandling.throw_error("Invalid character type", character_type)

    def get_characters(self):
        return self.__characters




