from pygame.image import load
from pygame.sprite import Sprite

from config import join, img_dir, SCREEN_WIDTH, SCREEN_HEIGHT, TILE


class Floor(Sprite):
    def __init__(self, app, image, position):
        self.app = app
        super(Floor, self).__init__(self.app.game.all_sprites)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)

class Map:
    def __init__(self, app):
        self.app = app
        self.image = load(join(img_dir, "wall", "floor.png")).convert_alpha()

    def draw(self):
        for x in range(0, SCREEN_WIDTH, TILE):
            for y in range(0, SCREEN_HEIGHT, TILE):
                Floor(app=self.app, image=self.image, position=(x, y))