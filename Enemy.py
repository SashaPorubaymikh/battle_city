from pygame.sprite import Sprite, collide_rect, Rect
from pygame import Surface
from Bullet import Bullet
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
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((40, 40))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.xvel = self.yvel = 0
        self.rect.x = x
        self.rect.y = y
        self.ready = False
        self.timer = 0
        self.MOVE_SPEED = 1
        self.lifes = 3
        self.dir = ''
        self.ldir = 'down'
        self.min_x = self.min_y = 100000

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

    def find_way(self, target_list, bullets_group):
        if len(target_list) > 0:
            for x in target_list:
                if abs(x.rect.x - self.rect.x) < self.min_x:
                    self.min_x = abs(x.rect.x - self.rect.x)
                if abs(x.rect.y - self.rect.y) < self.min_y:
                    self.min_y = abs(x.rect.y - self.rect.y)
            if self.min_x < self.min_y:
                if x.rect.x - self.rect.x > 0:
                    self.dir = 'right'
                    self.ldir = 'right'
                if x.rect.x - self.rect.x < 0:
                    self.dir = 'left'
                    self.ldir = 'left'
                if x.rect.x - self.rect.x == 0:
                    if x.rect.y - self.rect.y > 0:
                        self.dir = ''
                        self.ldir = 'down'
                        if self.ready:
                            self.shoot(self.ldir, bullets_group)
                            self.ready = False
                    if x.rect.y - self.rect.y < 0:
                        self.dir = ''
                        self.ldir = 'up'
                        if self.ready:
                            self.shoot(self.ldir, bullets_group)
                            self.ready = False
            else:
                if x.rect.y - self.rect.y < 0:
                    self.dir = 'up'
                    self.ldir = 'up'
                if x.rect.y - self.rect.y > 0:
                    self.dir = 'down'
                    self.ldir = 'down'
                if x.rect.y - self.rect.y == 0:
                    if x.rect.x - self.rect.x < 0:
                        self.dir = ''
                        self.ldir = 'left'
                        if self.ready:
                            self.shoot(self.ldir, bullets_group)
                            self.ready = False
                    if x.rect.x - self.rect.x > 0:
                        self.dir = ''
                        self.ldir = 'right'
                        if self.ready:
                            self.shoot(self.ldir, bullets_group)
                            self.ready = False
        else:
            self.dir = ''
                        
    def update(self, sprites, target_list, bullets_group, lvl_w, lvl_h, target_list_1):

        if self.ready == False:
            self.timer += 1
        if self.timer == 60:
            self.timer = 0
            self.ready = True
        self.xvel = self.yvel = 0
        self.min_x = self.min_y = 10000
        self.find_way(target_list, bullets_group)
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
        self.collide(self.xvel, 0, sprites)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, sprites)
        if self.lifes == 0:
            sprites.remove(self)
            target_list_1.remove(self)

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

    def shoot(self, dir, bullets_group):
        if dir == 'left':
            bull = Bullet(self.rect.x - 10, self.rect.y + 18, 'images/bullets/ebullet_ver.png', dir)
            bullets_group.append(bull)
        if dir == 'right':
            bull = Bullet(self.rect.x + 50, self.rect.y + 18, 'images/bullets/ebullet_ver.png', dir)
            bullets_group.append(bull)
        if dir == 'down':
            bull = Bullet(self.rect.x + 18, self.rect.y+40, 'images/bullets/pbullet_ver.png', dir)
            bullets_group.append(bull)
        if dir == 'up':
            bull = Bullet(self.rect.x + 18, self.rect.y+10, 'images/bullets/pbullet_ver.png', dir)
            bullets_group.append(bull)