from pygame.image import load
from pygame.sprite import Sprite

from config import join, img_dir, SCREEN_WIDTH, SCREEN_HEIGHT


class Map(Sprite):
    def __init__(self, app):
        self.app = app
        super().__init__(self.app.game.all_sprites)