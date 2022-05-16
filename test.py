from random import randint

from pygame import init, Surface, QUIT, KEYDOWN, K_ESCAPE
from pygame.display import set_mode, set_caption, flip
from pygame.event import get
from pygame.sprite import Sprite, Group
from pygame.time import Clock

init()

screen = set_mode((500, 500))
clock = Clock()


class Test(Sprite):
    def __init__(self):
        super(Test, self).__init__(all_sprites)
        self.image = Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(randint(0, 500), randint(0, 500)))
        self.count = 10
        self.speed = 5

    def update(self):
        self.count -= 1
        if self.count < 0:
            self.speed = -self.speed
            self.count = 10

        self.rect.x += self.speed


all_sprites = Group()
for _ in range(10 ** 3):
    Test()

print(len(all_sprites))

running = True
while running:
    clock.tick(60)

    for event in get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    set_caption(f'FPS: {clock.get_fps() :.2f}')
    flip()

