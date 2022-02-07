from math import hypot, degrees, atan2

from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, MOUSEBUTTONDOWN
from pygame.image import load
from pygame.key import get_pressed
from pygame.mouse import get_pos
from pygame.sprite import Sprite

from config import join, img_dir, SCREEN_WIDTH, SCREEN_HEIGHT
from data.core.weapon import Bullet


class Player(Sprite):
    def __init__(self, app):
        self.app = app
        super().__init__(self.app.game.all_sprites)
        self.image = load(join(img_dir, "char free", "player.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.speed = 5
        self.speed_x, self.speed_y = 0, 0

    def update(self):
        self.speed_x, self.speed_y = 0, 0
        key_pressed = get_pressed()
        if key_pressed[K_UP]: self.speed_y = -self.speed
        if key_pressed[K_DOWN]: self.speed_y = self.speed
        if key_pressed[K_LEFT]: self.speed_x = -self.speed
        if key_pressed[K_RIGHT]: self.speed_x = self.speed

        for event in self.app.events:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    Bullet(self.app, self.rect.center)

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
