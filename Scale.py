import pygame as pg


class Scale:
    @staticmethod
    def scale(image, x, y):
        # *4 Scaling
        scale = 4
        size = image.get_size()
        bigger_img = pg.transform.scale(image, (int(size[0]*scale), int(size[1]*scale)))
        image_rect = pg.Rect(x*scale, y*scale, size[0]*scale, size[1]*scale)

        return bigger_img, image_rect
