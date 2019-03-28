from pygame.sprite import Sprite, collide_rect
from pygame.image import load
from pygame.transform import rotate

class Bullet(Sprite):
    def __init__(self, x, y, image, direction):
        Sprite.__init__(self)
        self.image = load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = direction
        self.speed = 10

    def update(self, direction, screen, sprites, bullets_group, lvl_w, lvl_h):
        if self.dir == 'up':
            self.rect.y -= self.speed
        if self.dir == 'down':
            self.rect.y += self.speed
        if self.dir == 'left':
            self.rect.x -= self.speed
        if self.dir == 'right':
            self.rect.x += self.speed
        self.collide(sprites, bullets_group)
        if self.rect.x < 0 or self.rect.y < 0 or self.rect.x > lvl_w or self.rect.y > lvl_h:
            bullets_group.remove(self)

    def collide(self, sprites, bullets_group):
        for b in sprites:
            if collide_rect(self, b):
                b.lifes -= 1
                bullets_group.remove(self)
                break
        for b in bullets_group:
            if collide_rect(self, b) and b != self:
                bullets_group.remove(b)

