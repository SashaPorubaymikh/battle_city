from pygame.sprite import Sprite
from pygame.image import load
from pygame.transform import scale

class Blocks(Sprite):
    def __init__(self, x, y, image, lifes):
        Sprite.__init__(self)
        self.image = load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lifes = lifes
        self.type = 'block'
    def update(self, group):
        if self.lifes == 0:
            group.remove(self)    