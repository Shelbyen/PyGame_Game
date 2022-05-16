from pygame import MOUSEWHEEL, KEYDOWN, K_p
from pygame.sprite import Group

from core.button import Button
from data.core.camera import CameraGroup
from data.core.game_object import Props
from data.core.generation_map import Map
from data.core.initial import InitTextures
from data.core.player import Player
from debug import debug


class Game:
    def __init__(self, app):
        self.app = app

        self.camera_group = CameraGroup()
        self.buttons = Group()
        self.bullets = Group()
        self.walls = Group()
        self.bots = Group()

        self.textures = InitTextures()

        self.map = Map(self)
        self.map.draw()

        self.player = Player(self)
        self.props = Props(self)

    def draw(self):
        self.camera_group.custom_draw()
        if self.bots:
            debug(list(bot.position for bot in self.bots.sprites()), y=70)

    def update(self):
        self.props.update()

        for event in self.app.events:
            if event.type == MOUSEWHEEL:
                self.camera_group.zoom_scale += event.y * 0.03
            if event.type == KEYDOWN:
                if event.key == K_p:
                    self.app.change_status("Menu")

        self.camera_group.update()

    def run(self):
        self.update()
        self.draw()
