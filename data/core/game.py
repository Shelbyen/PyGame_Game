from pygame.sprite import Group

from data.core.camera import CameraGroup
from data.core.game_object import Props
from data.core.generation_map import Map
from data.core.initial import InitTextures
from data.core.player import Player


class Game:
    def __init__(self, app):
        self.app = app

        self.all_sprites = Group()
        self.bullets = Group()

        self.textures = InitTextures()

        self.camera_group = CameraGroup()

        self.map = Map(self)
        self.map.draw()

        self.player = Player(self)
        self.props = Props(self.app)

    def draw(self):
        self.all_sprites.draw(self.app.screen)

    def update(self):
        self.props.update()
        self.all_sprites.update()

    def run(self):
        self.update()
        self.draw()