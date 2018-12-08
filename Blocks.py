from pygame.sprite import Sprite
from pygame import image

class Block(Sprite):
    def __init__(self, x, y, image):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image.load(image)
        self.rect = self.image.get_rect()