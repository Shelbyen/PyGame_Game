from pygame import QUIT
from pygame.display import set_mode, flip, set_caption
from pygame.event import get
from pygame.time import Clock

from config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, BLACK, State
from data.core.game import Game
from data.core.menu import Menu


class App:
    def __init__(self):
        self.screen = set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = Clock()
        self.menu = Menu(self)
        self.game_state = self.menu
        self.events = None

    def change_status(self, state):
        if state == State.Menu.name and not isinstance(self.game_state, Menu):
            self.game_state = self.menu
        elif state == State.Game.name and not isinstance(self.game_state, Game) and isinstance(self.game_state, Menu):
            self.game_state = Game(self)

    def run(self):
        while True:
            flip()

            self.events = get()
            [exit() for event in self.events if event.type == QUIT]

            self.screen.fill(BLACK)

            self.game_state.run()

            self.clock.tick(FPS)
            set_caption(f"FPS: {self.clock.get_fps() :.2f}")


if __name__ == '__main__':
    app = App()
    app.run()
