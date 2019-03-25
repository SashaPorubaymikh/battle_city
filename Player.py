from pygame.sprite import Sprite, collide_rect
from pygame import image
from pygame import Surface
import pyganim

MOVE_SPEED = 1

ANIM_DELAY = 0.1
ANIMATION_STAY_UP = [('images/tanks/player_up_1.png', ANIM_DELAY)]
ANIMATION_STAY_DOWN = [('images/tanks/player_down_1.png', ANIM_DELAY)]
ANIMATION_STAY_LEFT = [('images/tanks/player_left_1.png', ANIM_DELAY)]
ANIMATION_STAY_RIGHT = [('images/tanks/player_right_1.png', ANIM_DELAY)]

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
        self.ready = True
        self.timer = 0

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

        self.boltAnimRight = make_boltAnimation(ANIMATION_RIGHT, ANIM_DELAY)
        self.boltAnimRight.play()

        self.boltAnimLeft = make_boltAnimation(ANIMATION_LEFT, ANIM_DELAY)
        self.boltAnimLeft.play()

        self.boltAnimUp = make_boltAnimation(ANIMATION_UP, ANIM_DELAY)
        self.boltAnimUp.play()

        self.boltAnimDown = make_boltAnimation(ANIMATION_DOWN, ANIM_DELAY)
        self.boltAnimDown.play()

    def update(self, left, right, up, down, lleft, lright, lup, ldown, blocks):
        if not(self.ready):
            self.timer += 1
        if self.timer == 10:
            self.timer = 0
            self.ready = True
        if left:
            self.xvel = -MOVE_SPEED
            self.boltAnimLeft.blit(self.image, (0, 0))
        if right:
            self.xvel = MOVE_SPEED
            self.boltAnimRight.blit(self.image, (0, 0))
        if up:
            self.yvel = -MOVE_SPEED
            self.boltAnimUp.blit(self.image, (0, 0))
        if down:
            self.yvel = MOVE_SPEED
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
        self.collide(self.xvel, 0, blocks)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, blocks)


    def collide(self, xvel, yvel, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                if yvel < 0:
                    self.rect.top = pl.rect.bottom
            