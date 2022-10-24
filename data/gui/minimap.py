from pygame import Surface
from pygame.draw import rect
from pygame.sprite import Sprite

from config import MINIMAP_SIZE, SCREEN_HEIGHT


class Minimap(Sprite):
    def __init__(self, menu):
        self.menu = menu
        super().__init__(self.menu.gui)
        self.image = Surface((MINIMAP_SIZE, MINIMAP_SIZE))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(topleft=(0, SCREEN_HEIGHT - MINIMAP_SIZE))

    def draw(self):
        x = y = 0
        for row in self.menu.map.level:  # вся строка
            for col in row:  # каждый символ
                if col == "Floor":
                    rect(self.menu.app.screen, (88, 88, 88), (x, y, x))
                elif col == 'Wall':
                    if random.randint(1, 100) <= 96:
                        Wall(game=self.game, position=(x, y), group=self.game.walls)
                    else:
                        Ore(game=self.game, position=(x, y), group=self.game.walls)

                x += TILE  # блоки платформы ставятся на ширине блоков
            y += TILE  # то же самое и с высотой
            x = 0
