from pygame import KEYDOWN, K_ESCAPE, MOUSEMOTION, MOUSEBUTTONDOWN, K_q, K_e
from pygame.sprite import Group

from data.core.camera import CameraGroup
from data.core.game_object import Props
from data.core.generation_map import Map
from data.core.initial import InitTextures
from data.core.pause_menu import PauseMenu
from data.core.player import Player
from data.gui.minimap import Minimap
from debug import debug


class Game:
    def __init__(self, app):
        self.app = app

        self.camera_group = CameraGroup()
        self.bullets = Group()
        self.walls = Group()
        self.bots = Group()
        self.factories = Group()
        self.gui = Group()

        self.textures = InitTextures()

        self.map = Map(self)
        self.map.draw()
        self.minimap = Minimap(self)

        self.player = Player(self)
        self.props = Props(self)

        self.state = [0]
        self.pause_menu = PauseMenu(self, self.app)

    def draw(self):
        self.camera_group.custom_draw()
        self.gui.draw(self.app.screen)
        self.pause_menu.draw()
        if self.bots:
            debug(list(bot.position for bot in self.bots.sprites()), y=70)

    def update(self):
        self.props.update()
        self.pause_menu.update()

        for event in self.app.events:
            if event.type == MOUSEMOTION:
                self.camera_group.keyboard_control(event)
            if event.type == MOUSEBUTTONDOWN:
                self.camera_group.zoom_control(event.button, event.pos)
            if event.type == KEYDOWN:
                if event.key == K_q:
                    self.camera_group.zoom_control(4)
                if event.key == K_e:
                    self.camera_group.zoom_control(5)
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
