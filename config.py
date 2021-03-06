from enum import Enum
from os.path import join, dirname


base_dir = dirname(__file__)
data_dir = join(base_dir, "data")
img_dir = join(data_dir, "img")
snd_dir = join(data_dir, "snd")
core_dir = join(data_dir, "core")


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
B_WIDTH = 256
B_HEIGHT = 82
B_INTERVAL = 6
TILE = 32
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class State(Enum):
    Menu = 0
    Game = 1
