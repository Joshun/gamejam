from Overlays.HudOverlay import HudOverlay
from Overlays.SceneIntro import SceneIntro
from Overlays.Inventory import Inventory
import pygame


class Overlay():
    """docstring for Overlay"""
    def __init__(self, player):
        self.scene_intro = None
        self.hud_overlay = HudOverlay(player)
        self.inventory = Inventory()
        self.inventory_visible = False

    def update_scene_intro(self, location, lines):
        self.scene_intro = SceneIntro(location, lines)

    def draw(self, screen):
        self.hud_overlay.draw(screen)

        if self.scene_intro:
            self.scene_intro.draw(screen)
        if self.inventory_visible:
            self.inventory.draw(screen)

    def update(self, keys):
        self.hud_overlay.update()

        if keys[pygame.K_o]:
            print ('Open inventory')
            self.inventory.open()
            self.inventory_visible = True
        elif self.inventory_visible:
            if keys[pygame.K_p]:
                self.inventory.close()
                self.inventory_visible = False

        if self.scene_intro:
            if keys[pygame.K_SPACE]:
                self.scene_intro.next()
                if self.scene_intro.closed:
                    self.scene_intro = None
