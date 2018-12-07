from pygame.sprite import Sprite
from pygame import image

class Player(Sprite):
    def __init__(self, x, y, image):
        Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y

    def update(self, left, right, up, down):
        if Left:
            self.x -= MOVE_SPEED
        if right:
            self.x += MOVE_SPEED
        if up:
            self.y -= MOVE_SPEED
        if down:
            self.y += MOVE_SPEED
    
    def draw(self, surf):
        surf.blit(self.image, (self.x, self.y))