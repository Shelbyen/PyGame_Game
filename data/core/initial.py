from pygame.image import load

from config import join, img_dir


class InitTextures:
    def __init__(self):
        self.floor = load(join(img_dir, "walls", "floor.png")).convert_alpha()
        self.wall = load(join(img_dir, "walls", "cube.png")).convert_alpha()
        self.ore = load(join(img_dir, "walls", "ore.png")).convert_alpha()
