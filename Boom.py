from pygame.image import load
from pygame import Surface

import pyganim

ANIMATION_DELAY = 0.07
ANIMATION_DELAY_1 = 0.15
boom_anim = [
    ('images/boom/boom_1.png', ANIMATION_DELAY),
    ('images/boom/boom_2.png', ANIMATION_DELAY),
    ('images/boom/boom_3.png', ANIMATION_DELAY),
    ('images/boom/boom_4.png', ANIMATION_DELAY),
    ('images/boom/boom_5.png', ANIMATION_DELAY),
    ('images/boom/boom_6.png', ANIMATION_DELAY),
    ('images/boom/boom_7.png', ANIMATION_DELAY),
]
boom_anim_1 = [
    ('images/boom/boom_1.1.png', ANIMATION_DELAY_1),
    ('images/boom/boom_2.1.png', ANIMATION_DELAY_1),
    ('images/boom/boom_3.1.png', ANIMATION_DELAY_1),
    ('images/boom/boom_4.1.png', ANIMATION_DELAY_1),
    ('images/boom/boom_5.1.png', ANIMATION_DELAY_1),
    ('images/boom/boom_6.1.png', ANIMATION_DELAY_1),
    ('images/boom/boom_7.1.png', ANIMATION_DELAY_1),
    ('images/boom/boom_8.1.png', ANIMATION_DELAY_1),
    ('images/boom/boom_9.1.png', ANIMATION_DELAY_1),
    ('images/boom/boom_10.1.png', ANIMATION_DELAY_1),
]

class Boom():
    def __init__(self, x, y, num):
        self.num = num
        if self.num == 0:
            self.image = Surface((60, 60))
            self.anim = pyganim.PygAnimation(boom_anim)
        else:
            self.image = Surface((700, 700))
            self.anim = pyganim.PygAnimation(boom_anim_1)
        self.rect = self.image.get_rect()
        
        self.image.set_colorkey((0, 0, 0))
        self.anim.play()
        self.timer = 0
        if self.num == 1:
            self.rect.x = x - 330
            self.rect.y = y - 330
        else:
            self.rect.x = x - 10
            self.rect.y = y - 10

    def update(self, boom_group):
        self.image.fill((0, 0, 0))
        self.anim.blit(self.image, (0, 0))
        self.timer += 1
        if (self.timer == 18 and self.num == 0) or (self.timer == 40):
            boom_group.remove(self)