from pygame.sprite import Group

from data.core.game_object import Props
from data.core.player import Player


class Game:
    def __init__(self, app):
        self.app = app

    def setup(self):
        self.all_sprites = Group()
        self.player = Player(self.app)
        self.props = Props(self.app)

    def draw(self):
        self.all_sprites.draw(self.app.screen)

    def update(self):
        self.props.update()
        self.all_sprites.update()

    def run(self):
        self.update()
        self.draw()
