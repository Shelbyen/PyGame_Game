from math import hypot, degrees, atan2

from pygame import Surface, K_e, K_q, K_DOWN, K_UP
from pygame.key import get_pressed
from pygame.mouse import get_pos
from pygame.sprite import Sprite
from pygame.transform import rotate


class Bullet(Sprite):
    def __init__(self, app, pos):
        self.app = app
        super(Bullet, self).__init__(self.app.game.all_sprites, self.app.game.bullets)

        self.pos = pos
        mx, my = get_pos()
        self.dir = (mx - self.pos[0], my - self.pos[1])
        length = hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = degrees(atan2(-self.dir[1], self.dir[0]))

        self.image = Surface((10, 2)).convert_alpha()
        self.image.fill((255, 255, 255))
        self.image = rotate(self.image, angle)

        self.rect = self.image.get_rect(center=self.pos)

        self.speed = 20

    def update(self):
        key_pressed = get_pressed()

        if key_pressed[K_UP]: self.speed += 1
        if key_pressed[K_DOWN] and self.speed > 1: self.speed -= 1

        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)
        self.rect = self.image.get_rect(center=self.pos)

        if not self.app.screen.get_rect().colliderect(self.rect):
            self.kill()
