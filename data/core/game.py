from pygame import MOUSEWHEEL
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

        self.map = Map(self, self.camera_group)
        self.map.draw()

        self.player = Player(self, self.camera_group)
        self.props = Props(self.app)

    def draw(self):
        self.all_sprites.draw(self.app.screen)

    def update(self):
        self.props.update()

        self.camera_group.update()
        self.camera_group.custom_draw()

        for event in self.app.events:
            if event.type == MOUSEWHEEL:
                self.camera_group.zoom_scale += event.y * 0.03

        self.all_sprites.update()

    def run(self):
        self.update()
        self.draw()