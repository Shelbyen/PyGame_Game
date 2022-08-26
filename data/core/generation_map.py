import random

import numpy as np
from pygame.sprite import Sprite
from scipy.ndimage.interpolation import zoom

from config import TILE


class Platform(Sprite):
    def __init__(self, game, position, image, group=[]):
        self.game = game
        super(Platform, self).__init__(self.game.camera_group, *group)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)


class Wall(Platform):
    def __init__(self, game, position, group):
        self.game = game
        super(Wall, self).__init__(self.game, position, self.game.textures.wall, group)


class Ore(Platform):
    def __init__(self, game, position, group):
        self.game = game
        super(Ore, self).__init__(self.game, position, self.game.textures.ore, group)


class Floor(Platform):
    def __init__(self, game, position):
        self.game = game
        super(Floor, self).__init__(self.game, position, self.game.textures.floor)


class Map:
    def __init__(self, game):
        self.game = game
        self.level = None
        self.generate_level()

    def generate_level(self):
        self.level = np.random.uniform(size=(10, 10))
        self.level = zoom(self.level, 12)
        self.level = self.level > 0.8
        self.level = np.where(self.level, 'Wall', 'Floor')

    def draw(self):
        x = y = 0
        for row in self.level:  # вся строка
            for col in row:  # каждый символ
                if col == "Floor":
                    Floor(game=self.game, position=(x, y))
                elif col == 'Wall':
                    if random.randint(1, 100) <= 96:
                        Wall(game=self.game, position=(x, y), group=self.game.walls)
                    else:
                        Ore(game=self.game, position=(x, y), group=self.game.walls)

                x += TILE  # блоки платформы ставятся на ширине блоков
            y += TILE  # то же самое и с высотой
            x = 0
