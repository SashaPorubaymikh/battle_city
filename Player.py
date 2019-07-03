from pygame.sprite import Sprite, collide_rect
from pygame import image
from pygame import Surface
from pygame.transform import scale

import pyganim, sys
from Boom import Boom
from dead import Dead

from Bullet import Bullet

ANIMATION_DELAY = 0.1

ANIMATION_STAY_UP = [('images/tanks/player_up_1.png', ANIMATION_DELAY)]
ANIMATION_STAY_DOWN = [('images/tanks/player_down_1.png', ANIMATION_DELAY)]
ANIMATION_STAY_LEFT = [('images/tanks/player_left_1.png', ANIMATION_DELAY)]
ANIMATION_STAY_RIGHT = [('images/tanks/player_right_1.png', ANIMATION_DELAY)]

ANIMATION_RIGHT = ['images/tanks/player_right_2.png',
                   'images/tanks/player_right_1.png'
]
ANIMATION_UP = ['images/tanks/player_up_2.png',
                'images/tanks/player_up_1.png'
]
ANIMATION_LEFT = ['images/tanks/player_left_2.png',
                  'images/tanks/player_left_1.png'
]
ANIMATION_DOWN = ['images/tanks/player_down_2.png',
                  'images/tanks/player_down_1.png'
]

class Player(Sprite):
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
        self.recharge = Surface((0, 5))
        self.recharge.fill((250, 0, 0))
        self.MOVE_SPEED = 2
        self.lifes = 3
        self.llifes = 3
        self.type = 'f'
        self.isdead = False
        self.dir = ''
        self.ldir = 'up'
        self.boom_showed = False

        #Создание анимации
        def make_boltAnimation(anim_list, delay):
            boltAnim = []
            for anim in anim_list:
                boltAnim.append((anim, delay))
            Anim = pyganim.PygAnimation(boltAnim)
            return Anim
        
        self.boltAnimStayUp = pyganim.PygAnimation(ANIMATION_STAY_UP)
        self.boltAnimStayRight = pyganim.PygAnimation(ANIMATION_STAY_RIGHT)
        self.boltAnimStayDown = pyganim.PygAnimation(ANIMATION_STAY_DOWN)
        self.boltAnimStayLeft = pyganim.PygAnimation(ANIMATION_STAY_LEFT)

        self.boltAnimStayDown.play()
        self.boltAnimStayLeft.play()
        self.boltAnimStayRight.play()
        self.boltAnimStayUp.play()

        self.boltAnimRight = make_boltAnimation(ANIMATION_RIGHT, ANIMATION_DELAY)
        self.boltAnimRight.play()

        self.boltAnimLeft = make_boltAnimation(ANIMATION_LEFT, ANIMATION_DELAY)
        self.boltAnimLeft.play()

        self.boltAnimUp = make_boltAnimation(ANIMATION_UP, ANIMATION_DELAY)
        self.boltAnimUp.play()

        self.boltAnimDown = make_boltAnimation(ANIMATION_DOWN, ANIMATION_DELAY)
        self.boltAnimDown.play()

    def update(self, sprites, screen, friends, boom_group, player_spavn):
        
            
        if not(self.ready):
            self.timer += 1
            self.recharge = Surface((self.timer, 5))
            self.recharge.fill((250 - self.timer * 6, self.timer * 6, 0))
        if self.timer == 40:
            self.timer = 0
            self.ready = True
            self.recharge = Surface((40, 5))
            self.recharge.fill((0, 250, 0))
        self.yvel = self.xvel = 0
        if self.dir == 'left':
            self.xvel = -self.MOVE_SPEED
            self.boltAnimLeft.blit(self.image, (0, 0))
        elif self.dir == 'right':
            self.xvel = self.MOVE_SPEED
            self.boltAnimRight.blit(self.image, (0, 0))
        elif self.dir == 'up':
            self.yvel = -self.MOVE_SPEED
            self.boltAnimUp.blit(self.image, (0, 0))
        elif self.dir == 'down':
            self.yvel = self.MOVE_SPEED
            self.boltAnimDown.blit(self.image, (0, 0))
        elif self.ldir == 'left' and self.dir == '':
            self.xvel = 0
            self.yvel = 0       
            self.boltAnimStayLeft.blit(self.image, (0, 0))
        elif self.ldir == 'right' and self.dir == '':
            self.xvel = 0
            self.yvel = 0
            self.boltAnimStayRight.blit(self.image, (0, 0))
        elif self.ldir == 'down' and self.dir == '':
            self.yvel = 0
            self.xvel = 0
            self.boltAnimStayDown.blit(self.image, (0, 0))
        if self.ldir == 'up' and self.dir == '':
            self.yvel = 0
            self.xvel = 0
            self.boltAnimStayUp.blit(self.image, (0, 0))
        
        self.MOVE_SPEED = 2
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, sprites)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, sprites)
        if self.lifes == 0: 
            #sprites.remove(self)
            self.isdead = True
            if self.boom_showed == False:
                boom_group.append(Boom(self.rect.x, self.rect.y, 0))
                self.boom_showed = True
            return 0
        # if self.llifes > self.lifes:
        #     self.rect.x = player_spavn[0]
        #     self.rect.y = player_spavn[1]
        #     self.llifes = self.lifes
        


    def collide(self, xvel, yvel, sprites):
        for pl in sprites:
            if collide_rect(self, pl) and pl != self:
                if isinstance(pl, Dead):
                    pl.rect.x += xvel
                    pl.rect.y += yvel
                    if xvel == 0 and yvel == 0:
                        if self.ldir == 'up':
                            self.rect.top = pl.rect.bottom
                        if self.ldir == 'down':
                            self.rect.bottom = pl.rect.top
                        if self.ldir == 'right':
                            self.rect.right = pl.rect.left
                        if self.ldir == 'left':
                            self.rect.left = pl.rect.right
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
            
    def shoot(self, bullets_group):
        self.ready = False
        self.timer = 0
        if self.ldir == 'left':
            bull = Bullet(self.rect.x - 10, self.rect.y + 18, 'images/bullets/pbullet_ver.png', self.ldir, 'f')
            bullets_group.append(bull)
        if self.ldir == 'right':
            bull = Bullet(self.rect.x + 50, self.rect.y + 18, 'images/bullets/pbullet_ver.png', self.ldir, 'f')
            bullets_group.append(bull)
        if self.ldir == 'down':
            bull = Bullet(self.rect.x + 18, self.rect.y+40, 'images/bullets/pbullet_ver.png', self.ldir, 'f')
            bullets_group.append(bull)
        if self.ldir == 'up':
            bull = Bullet(self.rect.x + 18, self.rect.y-10, 'images/bullets/pbullet_ver.png', self.ldir, 'f')
            bullets_group.append(bull)