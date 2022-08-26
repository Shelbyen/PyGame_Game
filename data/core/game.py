from pygame import KEYDOWN, K_ESCAPE
from pygame.sprite import Group

from data.core.camera import CameraGroup
from data.core.game_object import Props
from data.core.generation_map import Map
from data.core.initial import InitTextures
from data.core.pause_menu import PauseMenu
from data.core.player import Player
from debug import debug


class Game:
    def __init__(self, app):
        self.app = app

        self.camera_group = CameraGroup()
        self.bullets = Group()
        self.walls = Group()
        self.bots = Group()
        self.factories = Group()

        self.textures = InitTextures()

        self.map = Map(self)
        self.map.draw()

        self.player = Player(self)
        self.props = Props(self)

        self.state = [0]
        self.pause_menu = PauseMenu(self, self.app)

    def draw(self):
        self.camera_group.custom_draw()
        self.pause_menu.draw()
        if self.bots:
            debug(list(bot.position for bot in self.bots.sprites()), y=70)

    def update(self):
        self.props.update()
        self.pause_menu.gui.update()

        for event in self.app.events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if self.state != [0]:
                        if self.state[-1] != 0:
                            self.state[-1] -= 1
                        else:
                            self.state.pop(-1)
                        self.pause_menu.gui.remove()
                    else:
                        self.state = [1]

        self.camera_group.update()

    def run(self):
        self.update()
        self.draw()
