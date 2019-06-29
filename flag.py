from pygame import Surface
from pygame.image import load
from pygame.sprite import Sprite

class Flag(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/game_atributes/flag.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lifes = 1
        self.type = 'flag'
    def update(self, group):
        if self.lifes == 0:
            group.remove(self)
            return "game over"
