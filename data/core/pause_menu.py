from pygame.sprite import Group

from config import SCREEN_WIDTH, SCREEN_HEIGHT, B_HEIGHT, B_INTERVAL
from data.gui.button import Button
from data.gui.text_label import InputBox


class PauseMenu:
    def __init__(self, game, app):
        self.game = game
        self.app = app
        self.gui = Group()
        self.pause_menu = Group()
        self.save_menu = Group()

        self.return_button = Button(self,
                                    (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 1.5 * B_HEIGHT - B_INTERVAL),
                                    "return", self.return_to_game, group=self.pause_menu)

        self.go_to_save_menu = Button(self,
                                      (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - B_HEIGHT // 2 - B_INTERVAL // 2),
                                      "go_to_save", self.go_to_save, group=self.pause_menu)

        self.settings_button = Button(self,
                                      (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + B_HEIGHT // 2 + B_INTERVAL // 2),
                                      "settings", self.view_settings, group=self.pause_menu)

        self.menu_button = Button(self,
                                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 1.5 * B_HEIGHT + B_INTERVAL),
                                  "go_to_menu", self.go_to_menu, group=self.pause_menu)

        self.save_button = Button(self,
                                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 1.5 * B_HEIGHT + B_INTERVAL),
                                  "save_button", self.go_to_menu, group=self.save_menu)

        self.change_save_name = InputBox(self,
                                         (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                                         "save_menu_1", group=self.save_menu)

    def draw(self):
        if self.game.state == [1]:
            self.pause_menu.draw(self.game.app.screen)
        elif self.game.state == [1, 0]:
            self.save_menu.draw(self.game.app.screen)

    def update(self):
        if self.game.state == [1]:
            self.pause_menu.update()
        elif self.game.state == [1, 0]:
            self.save_menu.update()

    def view_settings(self):
        pass

    def go_to_save(self):
        self.game.state = [1, 0]
        self.gui.remove()

    def return_to_game(self):
        self.game.state = [0]
        self.gui.remove()

    def go_to_menu(self):
        self.game.app.change_status("Menu")
