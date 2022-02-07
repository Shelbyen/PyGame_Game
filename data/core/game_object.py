from pygame import MOUSEBUTTONDOWN, K_r, KEYDOWN
from pygame.draw import circle
from pygame.image import load
from pygame.mouse import get_pos
from pygame.sprite import Sprite

from config import join, img_dir


class Props:
    def __init__(self, app):
        self.app = app
        self.types = [Bots]
        self.type = self.types[0]

    def update(self):
        for event in self.app.events:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.type(self.app, event.pos)
        # mouse_position = get_pos()
        # if self.type == "House":
        #     House(self.app, mouse_position)


class Object(Sprite):
    def __init__(self, app):
        self.app = app
        super().__init__(self.app.game.all_sprites)


class Bots(Object):
    def __init__(self, app, pos):
        super(Bots, self).__init__(app)
        self.position = pos
        self.image = load(join(img_dir, "bot.png")).convert_alpha()
        self.rect = self.image.get_rect(center=self.position)
        self.speed = 5
        self.speed_x, self.speed_y = 0, 0
        self.mouse_positions = []
        self.choice_on = False

    def movement(self):
        new_pos = self.mouse_positions[0]

        for pos in self.mouse_positions:
            circle(self.app.screen, (0, 255, 255), (pos[0], pos[1]), 5)

        if new_pos[0] // 10 < self.rect.centerx // 10: self.speed_x = -self.speed
        elif new_pos[0] // 10 > self.rect.centerx // 10: self.speed_x = self.speed
        if new_pos[1] // 10 < self.rect.centery // 10: self.speed_y = -self.speed
        elif new_pos[1] // 10 > self.rect.centery // 10: self.speed_y = self.speed

        if self.mouse_positions and (abs(new_pos[0] - self.rect.centerx) < 10
                                     and abs(new_pos[1] - self.rect.centery) < 10):
            self.mouse_positions.pop(0)

    def choice(self):
        circle(self.app.screen, (255, 255, 255), (self.rect.centerx, self.rect.centery), 18, 16)

    def update(self):
        mouse_position = get_pos()

        self.speed_x, self.speed_y = 0, 0

        for event in self.app.events:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 3:
                    if self.rect.collidepoint(mouse_position):
                        if self.choice_on:
                            self.mouse_positions.clear()
                        self.choice_on = not self.choice_on

            elif event.type == KEYDOWN:
                if event.key == K_r and self.choice_on:
                    self.mouse_positions.append(mouse_position)

        if self.choice_on and self.mouse_positions:
            self.movement()
        if self.choice_on:
            self.choice()

        # print(degrees(atan2(mouse_position[0] - self.rect.centerx, mouse_position[1] - self.rect.centery)) // 1)

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
