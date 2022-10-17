from pygame import SRCALPHA, Surface
from pygame.display import get_surface
from pygame.mouse import get_pressed
from pygame.sprite import Group
from pygame.transform import scale

from config import SCREEN_WIDTH, SCREEN_HEIGHT


class CameraGroup(Group):
    def __init__(self):
        super().__init__()
        self.display_surface = get_surface()

        self.camera_x = 0
        self.camera_y = 0

        self.zoom_scale = 1
        self.internal_surf_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.internal_surf = Surface(self.internal_surf_size, SRCALPHA)

    def keyboard_control(self, event):
        keys = get_pressed()
        if keys[0]:
            self.camera_x -= event.rel[0] * self.zoom_scale
            self.camera_y -= event.rel[1] * self.zoom_scale

    def zoom_keyboard_control(self, event):
        mouse_pos_x = event.pos[0]
        mouse_pos_y = event.pos[1]
        jump_x = self.camera_x + mouse_pos_x * self.zoom_scale
        jump_y = self.camera_y + mouse_pos_y * self.zoom_scale

        if event.button == 4:
            self.zoom_scale = self.zoom_scale * 0.85

            self.camera_x = jump_x - mouse_pos_x * self.zoom_scale
            self.camera_y = jump_y - mouse_pos_y * self.zoom_scale

        if event.button == 5:
            self.zoom_scale = self.zoom_scale / 0.85

            self.camera_x = jump_x - mouse_pos_x * self.zoom_scale
            self.camera_y = jump_y - mouse_pos_y * self.zoom_scale

    def custom_draw(self):
        self.internal_surf.fill('#000000')

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            # filter(lambda sprite: internal_surf.get_rect().colliderect(sprite.rect)
            sprite_pos_x = int((sprite.rect.centerx - self.camera_x) / self.zoom_scale)
            sprite_pos_y = int((sprite.rect.centery - self.camera_y) / self.zoom_scale)
            sprite.image = scale(sprite.image, (sprite.rect.width / self.zoom_scale,
                                                sprite.rect.height / self.zoom_scale))
            self.display_surface.blit(sprite.image, (sprite_pos_x, sprite_pos_y))
