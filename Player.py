from pygame.sprite import Sprite
from pygame.image import load

class player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.xvel = self.yvel = 0