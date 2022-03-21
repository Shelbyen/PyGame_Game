from pygame import SRCALPHA, Surface, Rect, K_q, K_e, K_a, K_d, K_w, K_s
from pygame.display import get_surface
from pygame.key import get_pressed
from pygame.math import Vector2
from pygame.sprite import Group
from pygame.transform import scale

from config import SCREEN_WIDTH, SCREEN_HEIGHT


class CameraGroup(Group):
    def __init__(self):
        super().__init__()
        self.display_surface = get_surface()

        # camera offset
        self.offset = Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        # box setup
        self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = Rect(l, t, w, h)

        # camera speed
        self.keyboard_speed = 5
        self.mouse_speed = 0.2

        # zoom
        self.zoom_scale = 1
        self.internal_surf_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.internal_surf = Surface(self.internal_surf_size, SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center=(self.half_w, self.half_h))
        self.internal_surface_size_vector = Vector2(self.internal_surf_size)
        self.internal_offset = Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

    def keyboard_control(self):
        keys = get_pressed()
        if keys[K_a]: self.camera_rect.x -= self.keyboard_speed
        if keys[K_d]: self.camera_rect.x += self.keyboard_speed
        if keys[K_w]: self.camera_rect.y -= self.keyboard_speed
        if keys[K_s]: self.camera_rect.y += self.keyboard_speed

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']

    def zoom_keyboard_control(self):
        keys = get_pressed()
        if keys[K_q]:
            self.zoom_scale += 0.1
        if keys[K_e]:
            self.zoom_scale -= 0.1

    def custom_draw(self):
        self.keyboard_control()
        self.zoom_keyboard_control()

        self.internal_surf.fill('#000000')

        # active elements
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surf.blit(sprite.image, offset_pos)

        scaled_surf = scale(self.internal_surf, tuple(map(int, (self.internal_surface_size_vector * self.zoom_scale))))
        scaled_rect = scaled_surf.get_rect(center=(self.half_w, self.half_h))

        self.display_surface.blit(scaled_surf, scaled_rect)

