import pygame


class SpriteSheet:
    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """
        :param x: left co-ordinate
        :param y: top co-ordinate
        :param width: single image width
        :param height: single image height
        :return: sprite cut
        """
        """ Grab a single image out of a larger sprite sheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        color_key = image.get_at((1, 1))
        image.set_colorkey(color_key, pygame.RLEACCEL)

        return image
