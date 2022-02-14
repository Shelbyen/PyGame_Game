import numpy as np
from pygame.image import load
from pygame.sprite import Sprite

from scipy.ndimage.interpolation import zoom

from config import join, img_dir, SCREEN_WIDTH, SCREEN_HEIGHT, TILE


class Floor(Sprite):
    def __init__(self, app, image, position):
        self.app = app
        super(Floor, self).__init__(self.app.game.all_sprites)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)


class Wall(Sprite):
    def __init__(self, app, image, position):
        self.app = app
        super(Wall, self).__init__(self.app.game.all_sprites)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)


class Map:
    def __init__(self, app):
        self.app = app
        self.floor = load(join(img_dir, "walls", "floor.png")).convert_alpha()
        self.wall = load(join(img_dir, "walls", "cube.png")).convert_alpha()

    def generate_level(self):
        global level
        level = np.random.uniform(size=(15, 15))
        level = zoom(level, 12)
        level = level > 0.8
        level = np.where(level, 'Wall', 'Floor')

    def draw(self):
        self.generate_level()
        x = y = 0
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "Floor":
                    Floor(app=self.app, image=self.floor, position=(x, y))
                elif col == 'Wall':
                    Wall(app=self.app, image=self.wall, position=(x, y))

                x += TILE  # блоки платформы ставятся на ширине блоков
            y += TILE  # то же самое и с высотой
            x = 0