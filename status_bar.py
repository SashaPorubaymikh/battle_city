from pygame.image import load
from pygame import font
from pygame import Surface

class Status_bar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surface = Surface((360, 60))
        self.surface.fill((65, 56, 231))
        self.surface.set_colorkey((65, 56, 231))
        self.surface.set_alpha(200)
        self.image = load("images/status_bar/status_bar.png")
        self.hp_image = load('images/status_bar/hp.png')
        self.friend_image = load('images/tanks/player_up_1.png')
        self.friend_image.set_colorkey((255, 255, 255))
        self.enemy_image = load('images/tanks/enemy_up_1.png')
        self.enemy_image.set_colorkey((255, 255, 255))
        self.font = font.Font('fonts/ComicTalecopy.ttf', 32)


    def show(self, hp, friends, enemies, lvl, scr, scr_w):
        self.surface.blit(self.image, (0, 0))
        self.surface.blit(self.hp_image, (10, 10))
        self.surface.blit(self.font.render('X'+str(hp), 1, (255, 255, 255)), (55, 15))

        self.surface.blit(self.friend_image, (110, 10))
        self.surface.blit(self.font.render('X'+str(friends-1), 1, (255, 255, 255)), (155, 15))

        self.surface.blit(self.enemy_image, (210, 10))
        self.surface.blit(self.font.render('X'+str(enemies), 1, (255, 255, 255)), (255, 15))

        scr.blit(self.surface, (0, 10))
        scr.blit(self.font.render('Stage ' + str(lvl), 1, (255, 255, 255)), (1366- self.font.size('stage'+str(lvl))[0] - 20, 10))