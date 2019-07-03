from pygame.sprite import Sprite, collide_rect, Rect
from pygame.image import load
from pygame import Surface

class Dead(Sprite):
    def __init__(self, x, y, type, direction):
        Sprite.__init__(self)
        self.image = Surface((40, 40))
        self.type = type
        self.dir = direction
        if self.type == 1:
            if self.dir == 'up':
                self.image = load('images/tanks/player_up_dead.png')
            if self.dir == 'down':
                self.image = load('images/tanks/player_down_dead.png')
            if self.dir == 'right':
                self.image = load('images/tanks/player_right_dead.png')
            if self.dir == 'left':
                self.image = load('images/tanks/player_left_dead.png')
        if self.type == 2:
            if self.dir == 'up':
                self.image = load('images/tanks/enemy_up_dead.png')
            if self.dir == 'down':
                self.image = load('images/tanks/enemy_down_dead.png')
            if self.dir == 'right':
                self.image = load('images/tanks/enemy_right_dead.png')
            if self.dir == 'left':
                self.image = load('images/tanks/enemy_left_dead.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.xvel = self.yvel = 0
        self.rect.x = x
        self.rect.y = y
        self.MOVE_SPEED = 1
        self.lifes = 5
    
    def update(self, sprites):
        self.collide(self.xvel, 0, sprites)
    
    def collide(self, xvel, yvel, sprites):
        for pl in sprites:
            if collide_rect(self, pl) and pl != self:
                if pl.rect.x - self.rect.x >= 35 and abs(pl.rect.y - self.rect.y) <= 35: 
                    self.rect.right = pl.rect.left
                if pl.rect.x - self.rect.x <= 35 and abs(pl.rect.y - self.rect.y) <= 35:
                    self.rect.left = pl.rect.right
                if pl.rect.y - self.rect.y >= 35 and abs(pl.rect.x - self.rect.x) <= 35:
                    self.rect.bottom = pl.rect.top
                if pl.rect.y - self.rect.y <= 35 and abs(pl.rect.x - self.rect.x) <= 35:
                    self.rect.top = pl.rect.bottom