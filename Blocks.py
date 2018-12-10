from pygame.sprite import Sprite
from pygame.image import load

class Blocks(Sprite):
    def __init__(self, x, y, image):
        Sprite.__init__(self)
        self.image = load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    