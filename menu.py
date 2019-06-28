import pygame, sys

pygame.init()
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)
scr_h = infos.current_h

class Menu:
    def __init__(self, punkts = [120, 140, u'Punkt', (20, 20, 20), (50, 50, 50), 0]):
        self.punkts = punkts
    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self, screen, window):
        done = True
        font_menu = pygame.font.Font ('fonts/ComicTalecopy.ttf', 100)
        pygame.key.set_repeat(1, 100)
        pygame.mouse.set_visible(True)
        punkt = 0
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
                        return 'exit'
                    if e.key == pygame.K_UP:
                        if punkt >= 0:
                            punkt -= 1
                        if punkt == -1:
                            punkt = len(self.punkts)-1
                    if e.key == pygame.K_DOWN:
                        if punkt <= len(self.punkts):
                            punkt += 1
                        if punkt == len(self.punkts):
                            punkt = 0
                    if e.key == pygame.K_KP_ENTER or e.key == pygame.K_RETURN:
                        if punkt == 0:
                            done = False
                            return 'game'
                        if punkt == 2:
                            return 'exit'
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                        return 'game'
                    if punkt == 2:
                        return 'exit'

            window.blit(screen, (0, 0))
            pygame.display.flip()

punkts = [(90, scr_h - 368, u'New Game', (30, 30, 30), (252, 102, 12), 0, 450),
          (90, scr_h - 268, u'Options', (30, 30, 30), (252, 102, 12), 1, 450),
          (90, scr_h - 168, u'Quit Game', (30, 30, 30), (252, 102, 12), 2, 450)]

punkts1 = [(90, scr_h - 368, u'Resume', (30, 30, 30), (252, 102, 12), 0, 450),
           (90, scr_h - 268, u'Options', (30, 30, 30), (252, 102, 12), 1, 450),
           (90, scr_h - 168, u'Main menu', (30, 30, 30), (252, 102, 12), 2, 450)]
