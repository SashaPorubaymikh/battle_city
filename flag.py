from pygame import Surface
from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

class Flag(Sprite):
    def __init__(self, x, y, zoom):
        Sprite.__init__(self)
        self.image = load('images/game_atributes/flag.png')
        self.image = scale(self.image, (40 + 10 * (zoom - 1), 40 + 10 * (zoom - 1)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lifes = 1
        self.type = 'flag'
    def update(self, group):
        if self.lifes == 0:
            group.remove(self)
            return "game over"
