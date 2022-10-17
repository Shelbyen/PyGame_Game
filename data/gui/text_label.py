from os.path import join

from pygame import MOUSEBUTTONDOWN, KEYDOWN, K_RETURN, K_BACKSPACE
from pygame.image import load
from pygame.sprite import Sprite

from config import FONT, img_dir


class InputBox(Sprite):
    def __init__(self, menu, pos, name, group=None, text=''):
        self.menu = menu
        self.group = group
        if self.group is not None:
            super().__init__(self.group)
        super().__init__(self.menu.gui)
        self.image = load(join(img_dir, "labels", f"{name}.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))
        self.color = (0, 0, 0)
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
        if event.type == KEYDOWN:
            if self.active:
                if event.key == K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        for event in self.menu.app.events:
            self.handle_event(event)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+10))
