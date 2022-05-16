from os.path import join

from pygame.image import load
from pygame.sprite import Sprite

from config import SCREEN_WIDTH, SCREEN_HEIGHT, img_dir


class Button(Sprite):
    def __init__(self, menu, pos):
        self.menu = menu
        super().__init__(self.menu.buttons)
        self.image = load(join(img_dir, "buttons", "button.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1]))
