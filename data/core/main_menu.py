from pygame.sprite import Group

from config import SCREEN_WIDTH, SCREEN_HEIGHT, B_HEIGHT, B_INTERVAL
from data.gui.button import Button
from data.core.initial import InitTextures


class Menu:
    def __init__(self, app):
        self.app = app

        self.gui = Group()
        self.textures = InitTextures()

        self.play_button = Button(self,
                                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 1.5 * B_HEIGHT - B_INTERVAL),
                                  "play", self.play)

        self.load_button = Button(self,
                                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - B_HEIGHT // 2 - B_INTERVAL // 2),
                                  "load", self.pass_func)

        self.settings_button = Button(self,
                                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + B_HEIGHT // 2 + B_INTERVAL // 2),
                                  "settings", self.pass_func)

        self.exit_button = Button(self,
                                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 1.5 * B_HEIGHT + B_INTERVAL),
                                  "exit", exit)

    def draw(self):
        self.gui.draw(self.app.screen)

    def play(self):
        self.app.change_status("Game")

    def pass_func(self):
        pass

    def update(self):
        self.gui.update()

    def run(self):
        self.update()
        self.draw()
