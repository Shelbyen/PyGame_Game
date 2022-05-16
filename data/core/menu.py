from pygame import MOUSEBUTTONDOWN
from pygame.mouse import get_pos
from pygame.sprite import Group

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from core.button import Button
from core.game import Game
from data.core.initial import InitTextures


class Menu:
    def __init__(self, app):
        self.app = app

        self.buttons = Group()
        self.textures = InitTextures()

        self.play_button = Button(self, (SCREEN_WIDTH // 2 - 128, SCREEN_HEIGHT // 2))

    def draw(self):
        self.buttons.draw(self.app.screen)

    def update(self):
        mouse_pos = get_pos()
        if self.play_button.rect.collidepoint(mouse_pos):
            for event in self.app.events:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.app.change_status("Game")

    def run(self):
        self.update()
        self.draw()
