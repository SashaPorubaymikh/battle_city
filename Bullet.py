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

    def update(self, direction, screen, blocks, bullets_group, scr_w, scr_h):
        if self.dir == 'up':
            self.rect.y -= self.speed
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.dir == 'down':
            self.rect.y += self.speed
            screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.dir == 'left':
            self.rect.x -= self.speed
            screen.blit(rotate(self.image, 90), (self.rect.x, self.rect.y))
        if self.dir == 'right':
            self.rect.x += self.speed
            screen.blit(rotate(self.image, 90), (self.rect.x, self.rect.y))
        self.collide(blocks, bullets_group)
        if self.rect.x < 0 or self.rect.y < 0 or self.rect.x > scr_w or self.rect.y > scr_h:
            bullets_group.remove(self)

    def collide(self, blocks, bullets_group):
        print('ok')
        print(self)
        for b in blocks:
            if collide_rect(self, b):
                b.lifes -= 1
                bullets_group.remove(self)
                break

