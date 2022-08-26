from os.path import join

from pygame import MOUSEBUTTONDOWN
from pygame.image import load
from pygame.mouse import get_pos
from pygame.sprite import Sprite

from config import img_dir


class Button(Sprite):
    def __init__(self, menu, pos, name, func, group=None):
        self.menu = menu
        self.func = func
        self.group = group
        if self.group is not None:
            super().__init__(self.group)
        super().__init__(self.menu.gui)
        self.name = name
        self.image = load(join(img_dir, "buttons", f"{name}.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))

    def update(self):
        mouse_pos = get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.collide_button()
        else:
            self.image.set_alpha(255)

    def collide_button(self):
        self.image.set_alpha(180)
        for event in self.menu.app.events:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.func()
