''' (комментарии - это то что нужно для меню. наверное это бессмысленно вставлять, но кто его знает, может будет понятнее, что полезно)
import pygame, sys
pygame.init()

infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)
scr_w = infos.current_w
scr_h = infos.current_h
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.Surface((scr_w, scr_h))
full_screen = True

pygame.display.set_caption('Platformer')
'''
class Menu:
    def __init__(self, punkts = [120, 140, u'Punkt', (20, 20, 20), (50, 50, 50), 0]):
        self.punkts = punkts
    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self):
        done = True
        font_menu = pygame.font.Font ('fonts/ComicTalecopy.ttf', 100)
        pygame.key.set_repeat(1, 100)
        pygame.mouse.set_visible(True)
        punkt = 0
        print(len(self.punkts))
        while done:
            screen.fill((10, 10, 10))
            
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+i[6] and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                        if punkt == 0:
                            punkt = len(self.punkts)
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts):
                            punkt += 1
                        if punkt == len(self.punkts):
                            punkt = 0
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    if punkt == 2:
                        sys.exit()

            window.blit(screen, (0, 0))
            pygame.display.flip()
''' 
punkts = [(90, scr_h - 368, u'New Game', (30, 30, 30), (252, 102, 12), 0, 450),
          (90, scr_h - 268, u'Options', (30, 30, 30), (252, 102, 12), 1, 450),
          (90, scr_h - 168, u'Quit Game', (30, 30, 30), (252, 102, 12), 2, 450)]

punkts1 = [(90, scr_h - 368, u'Resume', (30, 30, 30), (252, 102, 12), 0, 450),
           (90, scr_h - 268, u'Options', (30, 30, 30), (252, 102, 12), 1, 450),
           (90, scr_h - 168, u'Quit', (30, 30, 30), (252, 102, 12), 2, 450)]

                                                                                Это было самое важное

game = Menu(punkts)
game.menu()

score = 0

done = True

pygame.key.set_repeat(1, 1)

class Platform:
    def __init__(self):
        self.image = pygame.image.load('Sprites/Platformer/brick.png')

def make_level(level, platform):
    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == '0':
                screen.blit(platform.image, (x, y))
            x += 40
        y += 40
        x = 0

level = ['00000000000000000000000000000000000000',
         '00                                  00',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                                    0',
         '0                0000                0',
         '00               0  0               00',
         '00000000000000000000000000000000000000']

platform = Platform()

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                game = Menu(punkts1)
                game.menu()

                                                     А это применение punkts1 

    screen.fill((30, 30, 30))

    make_level(level, platform)

    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(10)

                                                  (пример платформера, первый образец меню)
'''

