from pygame.sprite import Sprite, collide_rect, Rect
from pygame import Surface
from Bullet import Bullet
from Boom import Boom

import pyganim
import random

ANIMATION_DELAY = 0.1

ANIMATION_STAY_UP = [('images/tanks/enemy_up_1.png', ANIMATION_DELAY)]
ANIMATION_STAY_DOWN = [('images/tanks/enemy_down_1.png', ANIMATION_DELAY)]
ANIMATION_STAY_LEFT = [('images/tanks/enemy_left_1.png', ANIMATION_DELAY)]
ANIMATION_STAY_RIGHT = [('images/tanks/enemy_right_1.png', ANIMATION_DELAY)]

ANIMATION_RIGHT = ['images/tanks/enemy_right_2.png',
                   'images/tanks/enemy_right_1.png'
]
ANIMATION_UP = ['images/tanks/enemy_up_2.png',
                'images/tanks/enemy_up_1.png'
]
ANIMATION_LEFT = ['images/tanks/enemy_left_2.png',
                  'images/tanks/enemy_left_1.png'
]
ANIMATION_DOWN = ['images/tanks/enemy_down_2.png',
                  'images/tanks/enemy_down_1.png'
]

class Enemy(Sprite):
    def __init__(self, x, y, diff):
        Sprite.__init__(self)
        self.image = Surface((40, 40))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.xvel = self.yvel = 0
        self.rect.x = x
        self.rect.y = y
        self.ready = False
        self.timer = 0
        self.MOVE_SPEED = 2
        if diff == 2:
            self.MOVE_SPEED = 4
        self.lifes = 1
        if diff == 2:
            self.lifes = 2
        self.min_x = self.min_y = 100000
        self.dirs = ["up", "down", "left", "right"]
        random.shuffle(self.dirs)
        self.dir = self.ldir = self.dirs[0]
        self.type = 'e'

        def make_anim(anim_list, delay):
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim

        self.AnimStayUp = pyganim.PygAnimation(ANIMATION_STAY_UP)
        self.AnimStayRight = pyganim.PygAnimation(ANIMATION_STAY_RIGHT)
        self.AnimStayDown = pyganim.PygAnimation(ANIMATION_STAY_DOWN)
        self.AnimStayleft = pyganim.PygAnimation(ANIMATION_STAY_LEFT)

        self.AnimGoUp = make_anim(ANIMATION_UP, ANIMATION_DELAY)
        self.AnimGoRight = make_anim(ANIMATION_RIGHT, ANIMATION_DELAY)
        self.AnimGoDown = make_anim(ANIMATION_DOWN, ANIMATION_DELAY)
        self.AnimGoLeft = make_anim(ANIMATION_LEFT, ANIMATION_DELAY)

        self.AnimGoDown.play()
        self.AnimGoLeft.play()
        self.AnimGoRight.play()
        self.AnimGoUp.play()
        self.AnimStayDown.play()
        self.AnimStayleft.play()
        self.AnimStayRight.play()
        self.AnimStayUp.play()

    def update(self, sprites, friends, enemies, bullets_group, lvl_w, lvl_h, boom_group):

        if self.ready == False:
            self.timer += 1
        if self.timer == 60:
            self.shoot(self.dir, bullets_group)
        self.xvel = self.yvel = 0
        self.min_x = self.min_y = 10000
        if self.dir == 'up':
            self.yvel = -self.MOVE_SPEED
            self.AnimGoUp.blit(self.image, (0, 0))
        if self.dir == 'down':
            self.yvel = self.MOVE_SPEED
            self.AnimGoDown.blit(self.image, (0, 0))
        if self.dir =='right':
            self.xvel = self.MOVE_SPEED
            self.AnimGoRight.blit(self.image, (0, 0))
        if self.dir == 'left':
            self.xvel = -self.MOVE_SPEED
            self.AnimGoLeft.blit(self.image, (0, 0))  
        if self.ldir == 'down' and self.dir == '':
            self.AnimStayDown.blit(self.image, (0, 0))
        if self.ldir == 'left' and self.dir == '':
            self.AnimStayleft.blit(self.image, (0, 0))
        if self.ldir == 'right' and self.dir == '':
            self.AnimStayRight.blit(self.image, (0, 0))
        if self.ldir == 'up' and self.dir == '':
            self.AnimStayUp.blit(self.image, (0, 0))
        self.rect.x += self.xvel
        if self.collide(self.xvel, 0, sprites):
            random.shuffle(self.dirs)
            self.dir = self.ldir = self.dirs[0]
        self.rect.y += self.yvel
        if self.collide(0, self.yvel, sprites):
            random.shuffle(self.dirs)
            self.dir = self.ldir = self.dirs[0]
        if self.lifes == 0:  
            sprites.remove(self)   
            boom_group.append(Boom(self.rect.x, self.rect.y, 0))
            return 0
        if friends == 0: 
            self.dir = ''
        if random.randint(0, 30) == 1 and self.rect.x % 10 == 0 and self.rect.y % 10 == 0:
            random.shuffle(self.dirs)
            self.dir = self.ldir = self.dirs[0]

    def collide(self, xvel, yvel, sprites):
        for pl in sprites:
            if collide_rect(self, pl) and pl != self:
                if xvel > 0:
                    self.rect.right = pl.rect.left

                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
                return True

    def shoot(self, dir, bullets_group):
        self.ready = False
        self.timer = 0
        if dir == 'left':
            bull = Bullet(self.rect.x - 10, self.rect.y + 18, 'images/bullets/ebullet_ver.png', dir, 'e')
            bullets_group.append(bull)
        if dir == 'right':
            bull = Bullet(self.rect.x + 50, self.rect.y + 18, 'images/bullets/ebullet_ver.png', dir, 'e')
            bullets_group.append(bull)
        if dir == 'down':
            bull = Bullet(self.rect.x + 18, self.rect.y+40, 'images/bullets/ebullet_ver.png', dir, 'e')
            bullets_group.append(bull)
        if dir == 'up':
            bull = Bullet(self.rect.x + 18, self.rect.y-10, 'images/bullets/ebullet_ver.png', dir, 'e')
            bullets_group.append(bull)