from Rooms.Wall import *

class InteractableObject(Wall):
    def __init__(self, rect, overlay, description, reset=True):
        super().__init__(rect, solid=False)
        self.__description = description
        self.__overlay = overlay
        self.__reset = reset
        self.__shown = False

    def display_text(self):
        if not self.__shown:
            self.__overlay.update_scene_intro("...", [self.__description])
            self.__shown = True

    def reset(self):
        if self.__reset:
            self.__shown = False


