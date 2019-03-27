from pygame.sprite import Sprite, collide_rect
from pygame import Surface

ANIMATION_STAY_UP = [('images/tanks/enemy_up_1.png', ANIM_DELAY)]
ANIMATION_STAY_DOWN = [('images/tanks/enemy_down_1.png', ANIM_DELAY)]
ANIMATION_STAY_LEFT = [('images/tanks/enemy_left_1.png', ANIM_DELAY)]
ANIMATION_STAY_RIGHT = [('images/tanks/enemy_right_1.png', ANIM_DELAY)]

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

ANIMATION_DELAY = 0.1

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
        self.lifes = 1
        self.way = []
        self.way_finder = Sirface((40, 40))
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

    def find_way(self, target list):
        for x in target_list:
            if abs(x.rect.x - self.rect.x) < self.min_x:
                self.min_x = abs(x.rect.x - self.rect.x)
            if abs(x.rect.y - self.rect.y) < self.min_y:
                self.min_y = abs(x.rect.y - self.rect.y)
            if self.min_x < self min_y:
                if x.rect.x - self.rect.x > 0
                    self.dir = 'right'
                if x.rect.x - self.rect.x < 0:
                    self.dir = 'left'
                if x.rect.x - self.rect.x == 0:
                    if x.rect.y - self.rect.y > 0:
                        self.dir = 'down'
                    if x.rect.y - self.rect.y < 0:
                        self.dir = 'up'
            else:
                if x.rect.y - self.rect.y < 0:
                    self.dir = 'up'
                if x.rect.y - self.rect.y > 0:
                    self.dir = 'down'
                if x.rect.y - self.rect.y == 0:
                    if x.rect.x - self.rect.x < 0:
                        self.dir = 'left'
                    if x.rect.x - self.rect.x > 0:
                        self.dir = 'right'
    def update(self, dir):
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
            self.xvel = self.MOVE_SPEED
            self.AnimGoLeft.blit(self.image, (0, 0))
        
        

    def collide(self, xvel, yvel, sprites):
        for pl in sprites:
            if collide_rect(self, pl):
                if xvel > 0:
                    self.rect.right = pl.rect.left
                if xvel < 0:
                    self.rect.left = pl.rect.right
                if yvel > 0:
                    self.rect.bottom = pl.rect.top
                if yvel < 0:
                    self.rect.top = pl.rect.bottom

    def shoot(self, dir):
        if dir == 'left':
            bull = Bullet(self.rect.x, self.rect.y + 18, 'images/bullets/ebullet_ver.png', dir)
            bullets_group.append(bull)
        if dir == 'right':
            bull = Bullet(self.rect.x, self.rect.y + 18, 'images/bullets/ebullet_ver.png', dir)
            bullets_group.append(bull)
        if dir == 'down'
            bull = Bullet(self.rect.x + 18, self.rect.y+30, 'images/bullets/pbullet_ver.png', dir)
            bullets_group.append(bull)
        if dir == 'up'
            bull = Bullet(self.rect.x + 18, self.rect.y, 'images/bullets/pbullet_ver.png', dir)
            bullets_group.append(bull)