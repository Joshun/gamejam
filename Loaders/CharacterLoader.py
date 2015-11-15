from Entities import FireElemental, NPC

from Steve import AwfulErrorHandling

class CharacterLoader:

    def __create_enemy(self, pos, speed, enemy_type):
        if enemy_type == "fire_elemental":
            return FireElemental
        else:
            AwfulErrorHandling.throw_error("Invalid enemy", enemy_type)

    def __init__(self, character_tiles):
        characters = []
        for character_obj in character_tiles:
            x = character_obj.x
            y = character_obj.y
            pos = (x,y)
            properties = character_obj.properties
            speed = properties["speed"]
            character_type = properties["character"]

            if character_type == "enemy":
                characters.append(self.__create_enemy(pos, speed, properties["enemy_type"]))
            elif character_type == "npc":
                characters.append(NPC(pos))
            else:
                AwfulErrorHandling.throw_error("Invalid character type", character_type)

        return characters





