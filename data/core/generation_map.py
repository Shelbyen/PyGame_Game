from typing import Any

import numpy as np
from pygame.display import get_surface
from pygame.sprite import Sprite
from scipy.ndimage.interpolation import zoom

from config import TILE


class Saver:
    def __init__(self, game):
        self.game = game
        self.blocks = []

    def uploader(self, pos_x, pos_y, name):
        self.blocks.append((pos_x, pos_y, name))

    def update(self):
        for block in self.blocks:
            if get_surface().get_rect().collidepoint(block[0], block[1]):
                if block[2] == "Floor":
                    Floor(self.game, (block[0], block[1]))
                elif block[2] == "Wall":
                    Wall(self.game, (block[0], block[1]), self.game.walls)
                self.blocks.remove(block)


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

    def update(self):
        if not get_surface().get_rect().colliderect(self.rect):
            Saver.uploader(self.game.saver, self.rect.centerx, self.rect.centery, "Wall")
            self.kill()


class Floor(Platform):
    def __init__(self, game, position):
        self.game = game
        super(Floor, self).__init__(self.game, position, self.game.textures.floor)

    def update(self):
        if not get_surface().get_rect().colliderect(self.rect):
            Saver.uploader(self.game.saver, self.rect.centerx, self.rect.centery, "Floor")
            self.kill()


class Map:
    def __init__(self, game):
        self.game = game
        self.level = None
        self.generate_level()

    def generate_level(self):
        self.level = np.random.uniform(size=(15, 15))
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
                    Wall(game=self.game, position=(x, y), group=self.game.walls)

                x += TILE  # блоки платформы ставятся на ширине блоков
            y += TILE  # то же самое и с высотой
            x = 0
