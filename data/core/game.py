from pygame import KEYDOWN, K_ESCAPE
from pygame.sprite import Group

from config import SCREEN_WIDTH, SCREEN_HEIGHT, B_HEIGHT, B_INTERVAL
from data.core.camera import CameraGroup
from data.core.game_object import Props
from data.core.generation_map import Map
from data.core.initial import InitTextures
from data.core.player import Player
from data.gui.button import Button
from debug import debug


class Game:
    def __init__(self, app):
        self.app = app

        self.pause = False

        self.camera_group = CameraGroup()
        self.buttons = Group()
        self.bullets = Group()
        self.walls = Group()
        self.bots = Group()
        self.factories = Group()

        self.textures = InitTextures()

        self.map = Map(self)
        self.map.draw()

        self.player = Player(self)
        self.props = Props(self)

        self.play_button = Button(self,
                                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - B_HEIGHT - B_INTERVAL),
                                  "return", self.return_to_game)

        self.settings_button = Button(self,
                                      (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                                      "settings", self.view_settings)

        self.menu_button = Button(self,
                                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + B_HEIGHT + B_INTERVAL),
                                  "go_to_menu", self.go_to_menu)

    def draw(self):
        self.camera_group.custom_draw()
        if self.pause:
            self.buttons.draw(self.app.screen)
        if self.bots:
            debug(list(bot.position for bot in self.bots.sprites()), y=70)

    def update(self):
        self.props.update()
        self.buttons.update()

        for event in self.app.events:
            # if event.type == MOUSEWHEEL:
            #     self.camera_group.zoom_scale += event.y * 0.03
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.pause = not self.pause

        self.camera_group.update()

    def view_settings(self):
        pass

    def return_to_game(self):
        self.pause = False

    def go_to_menu(self):
        self.app.change_status("Menu")

    def run(self):
        self.update()
        self.draw()
