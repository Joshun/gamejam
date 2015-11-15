import pygame as pg


class Scale:
    @staticmethod
    def scale(image, x, y):
        # *4 Scaling
        size = image.get_size()
        bigger_img = pg.transform.scale(image, (int(size[0]*4), int(size[1]*4)))
        image_rect = pg.Rect(x*4, y*4, size[0]*4, size[1]*4)

        return bigger_img, image_rect
