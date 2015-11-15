from Entities.FireElemental import FireElemental
from Entities.Player import Player
from Overlays.Overlay import Overlay
from Rooms.RoomCollection import *
from Entities.NPC import NPC

class Game(object):

    def __init__(self):
        """Initalize the display and prepare game objects."""
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 30.0
        self.keys = pg.key.get_pressed()
        self.done = False
        self.viewport = self.screen.get_rect()
        self.level = pg.Surface((1000, 1000)).convert()
        self.level_rect = self.level.get_rect()
        self.player = Player((40, 40), 100)
        self.delta_time = 0
        self.overlay = Overlay(self.player)
        self.enemy = FireElemental((100, 100), 1, 10)

        self.generic = NPC((200, 200))

        self.room_collection = RoomCollection("Rooms/RoomDescriptions.json", self.overlay)
        self.room_collection.get_current().set_room_collection(self.room_collection)

        entry_point = self.room_collection.get_current().get_entry_point()
        self.player.move_to(entry_point.x, entry_point.y)

    def update_viewport(self):
        """
        The viewport will stay centered on the player unless the player
        approaches the edge of the map.
        """
        self.viewport.center = self.player.rect.center
        self.viewport.clamp_ip(self.level_rect)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True

    def update(self):
        """Update the player and current viewport."""
        self.keys = pg.key.get_pressed()
        self.update_viewport()
        self.player.update(self.keys, self.delta_time)
        self.generic.update(self.delta_time)
        self.enemy.update(self.delta_time, self.player)
        self.overlay.update(self.keys)
        self.room_collection.update_current(self.screen, self.player)
        self.enemy.weapon.shoot(self.enemy.rect.centerx, self.enemy.rect.centery,"right")

    def draw(self):
        """
        Draw all necessary objects to the level surface, and then draw
        the viewport section of the level to the display surface.
        """
        self.level.fill(pg.Color("black"))
        self.room_collection.draw_current(self.level)
        self.player.draw(self.level)
        self.enemy.draw(self.level)
        self.generic.draw(self.level)
        self.screen.blit(self.level, (0, 0), self.viewport)
        self.overlay.draw(self.screen)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.delta_time = self.clock.tick(self.fps)

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("Game")
    pg.display.set_mode((800, 400))

    game = Game()
    game.main_loop()

    pg.quit()
    sys.exit()
