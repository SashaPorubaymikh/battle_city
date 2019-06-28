from pygame.sprite import Sprite, collide_rect
from pygame import image
from pygame import Surface
from pygame.transform import scale
import pyganim, sys

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
        self.MOVE_SPEED = 1
        self.lifes = 3
        self.type = 'f'

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

    def update(self, left, right, up, down, lleft, lright, lup, ldown, sprites, screen, friends):
        
            
        if not(self.ready):
            self.timer += 1
            self.recharge = Surface((self.timer, 5))
            self.recharge.fill((250 - self.timer * 6, self.timer * 6, 0))
        if self.timer == 40:
            self.timer = 0
            self.ready = True
            self.recharge = Surface((40, 5))
            self.recharge.fill((0, 250, 0))
        #screen.blit(self.recharge, (self.rect.x, self.rect.y - 10))
        if left:
            self.xvel = -self.MOVE_SPEED
            self.boltAnimLeft.blit(self.image, (0, 0))
        if right:
            self.xvel = self.MOVE_SPEED
            self.boltAnimRight.blit(self.image, (0, 0))
        if up:
            self.yvel = -self.MOVE_SPEED
            self.boltAnimUp.blit(self.image, (0, 0))
        if down:
            self.yvel = self.MOVE_SPEED
            self.boltAnimDown.blit(self.image, (0, 0))
        if lleft and not(left):
            self.yvel = 0
            self.xvel = 0
            self.boltAnimStayLeft.blit(self.image, (0, 0))
        if lright and not(right):
            self.yvel = 0
            self.xvel = 0
            self.boltAnimStayRight.blit(self.image, (0, 0))
        if ldown and not(down):
            self.yvel = 0
            self.xvel = 0
            self.boltAnimStayDown.blit(self.image, (0, 0))
        if lup and not(up):
            self.yvel = 0
            self.xvel = 0
            self.boltAnimStayUp.blit(self.image, (0, 0))
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, sprites)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, sprites)
        if self.lifes == 0: 
            sprites.remove(self)
            return 0


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
            