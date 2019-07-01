from pygame import Surface
from pygame.image import load
from pygame.sprite import Sprite

from Boom import Boom

class Dynamite(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('images/game_atributes/bomb.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lifes = 1
        self.type = 'bomb'
        self.timer = 2400
    def update(self, group, boom_group):
        if self.lifes == 0:
            group.remove(self)
            return "u win"
        self.timer -= 1
        if self.timer == 0:
            group.remove(self)
            boom_group.append(Boom(self.rect.x, self.rect.y, 1))
            return 'u lose'
