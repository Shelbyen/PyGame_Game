from pygame import QUIT
from pygame.display import set_mode, flip, set_caption
from pygame.event import get
from pygame.time import Clock

from config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, BLACK
from data.core.game import Game


class App:
    def __init__(self):
        self.screen = set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = Clock()
        self.game = Game(self)
        self.game.setup()
        self.events = None

    def run(self):
        while True:
            flip()

            self.events = get()
            [exit() for event in self.events if event.type == QUIT]

            self.screen.fill(BLACK)

            self.game.run()

            self.clock.tick(FPS)
            set_caption(f"FPS: {self.clock.get_fps() :.2f}")


if __name__ == '__main__':
    app = App()
    app.run()
