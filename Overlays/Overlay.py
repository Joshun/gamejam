from Overlays.HudOverlay import HudOverlay
from Overlays.SceneIntro import SceneIntro
import pygame


class Overlay():
    """docstring for Overlay"""
    def __init__(self, player):
        self.scene_intro = None
        self.hud_overlay = HudOverlay(player)
        self.current = self.scene_intro

    def update_scene_intro(self, location, lines):
        self.scene_intro = SceneIntro(location, lines)
        self.current = self.scene_intro

    def draw(self, screen):
        self.current.draw(screen)

    def update(self, keys):
        if self.current == self.scene_intro:
            if keys[pygame.K_SPACE]:
                self.scene_intro.next()
                if self.scene_intro.closed:
                    self.current = self.hud_overlay
        else:
            self.hud_overlay.update(keys)
