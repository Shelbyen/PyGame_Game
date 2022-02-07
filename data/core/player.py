from math import hypot, degrees, atan2

from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.image import load
from pygame.key import get_pressed
from pygame.mouse import get_pos
from pygame.sprite import Sprite

from config import join, img_dir, SCREEN_WIDTH, SCREEN_HEIGHT


class Player(Sprite):
    def __init__(self, app):
        self.app = app
        super().__init__(self.app.game.all_sprites)
        self.image = load(join(img_dir, "char free", "player.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.speed = 5
        self.speed_x, self.speed_y = 0, 0

    def bullet(self):
        pos = (self.rect.centerx, self.rect.centery)
        mx, my = get_pos()
        dir = (mx - pos[0], my - pos[1])
        length = hypot(*self.dir)
        if length == 0.0:
            dir = (0, -1)
        else:
            dir = (dir[0] / length, dir[1] / length)

        angle = degrees(atan2(-self.dir[1], self.dir[0]))

        self.bullet = self.app.screen((7, 2)).convert_alpha()
        self.bullet.fill((255, 255, 255))
        self.bullet = transform.rotate(self.bullet, angle)

    def update(self):
        mx, my = get_pos()

        self.speed_x, self.speed_y = 0, 0
        key_pressed = get_pressed()
        if key_pressed[K_UP]: self.speed_y = -self.speed
        if key_pressed[K_DOWN]: self.speed_y = self.speed
        if key_pressed[K_LEFT]: self.speed_x = -self.speed
        if key_pressed[K_RIGHT]: self.speed_x = self.speed

        self.dir = (mx - x, my - y)

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
