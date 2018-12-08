from pygame.sprite import Sprite
from pygame.image import load

class Blocks(Sprite):
    def __init__(self, x, y, image):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = load(image)

    def draw(self, surf):
        surf.blit(self.image, (self.x, self.y))
    