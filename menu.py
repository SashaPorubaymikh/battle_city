import pygame, sys

pygame.init()
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)
scr_h = infos.current_h
scr_w = infos.current_w

class Menu:
    def __init__(self, punkts, title):
        self.punkts = punkts
        self.title = title
        self.font_menu = pygame.font.Font('fonts/ComicTalecopy.ttf', 100)
        self.font_title = pygame.font.Font('fonts/ComicTalecopy.ttf', 150)
    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self, screen, window):
        done = True
        pygame.key.set_repeat(0, 500)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.fill((10, 10, 10))
            
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+i[6] and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, self.font_menu, punkt)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
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
                            return 'new game'
                        if punkt == 1:
                            return 'options'
                        if punkt == 2:
                            return 'exit'
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                        return 'new game'
                    if punkt == 1:
                        return 'options'
                    if punkt == 2:
                        return 'exit'

            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

class Pause:
    def __init__(self, punkts, title):
        self.punkts = punkts
        self.title = title
        self.font_menu = pygame.font.Font('fonts/ComicTalecopy.ttf', 100)
        self.font_title = pygame.font.Font('fonts/ComicTalecopy.ttf', 150)
    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self, screen, window):
        done = True
        pygame.key.set_repeat(0, 500)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.fill((10, 10, 10))
            
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+i[6] and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, self.font_menu, punkt)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
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
                            return 'new game'
                        if punkt == 1:
                            return 'restart'
                        if punkt == 2:
                            return 'exit'
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                        return 'resume'
                    if punkt == 1:
                        return 'restart'
                    if punkt == 2:
                        return 'exit'

            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

class Options:
    def __init__(self, punkts, title):
        self.punkts = punkts
        self.title = title
        self.font_menu = pygame.font.Font('fonts/ComicTalecopy.ttf', 100)
        self.font_title = pygame.font.Font('fonts/ComicTalecopy.ttf', 150)
        self.difficulties = ['easy', 'normal', 'hard']
        self.dif_punkt = 0
    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                if i[5] == 0:
                    surface.blit(font.render(i[2] + self.difficulties[self.dif_punkt], 1, i[4]), (i[0], i[1]))
                else:
                    surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                if i[5] == 0:
                    surface.blit(font.render(i[2] + self.difficulties[self.dif_punkt], 1, i[3]), (i[0], i[1]))
                else:
                    surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self, screen, window, dif_punkt):
        done = True
        pygame.key.set_repeat(0, 500)
        pygame.mouse.set_visible(True)
        punkt = 0
        self.dif_punkt = dif_punkt
        while done:
            screen.fill((10, 10, 10))
            
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+i[6] and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, self.font_menu, punkt)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
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
                        if punkt == 1:
                            return self.dif_punkt
                    if e.key == pygame.K_RIGHT:
                        if punkt == 0:
                            self.dif_punkt += 1
                            if self.dif_punkt == len(self.difficulties):
                                self.dif_punkt = 0
                    if e.key == pygame.K_LEFT:
                        if punkt == 0:
                            self.dif_punkt -= 1
                            if self.dif_punkt == -1:
                                self.dif_punkt = len(self.difficulties) - 1
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if punkt == 1:
                            return self.dif_punkt

            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

class End_of_game:
    def __init__(self, punkts, title):
        self.punkts = punkts
        self.title = title
        self.font_menu = pygame.font.Font('fonts/ComicTalecopy.ttf', 100)
        self.font_title = pygame.font.Font('fonts/ComicTalecopy.ttf', 150)
    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self, screen, window):
        done = True
        pygame.key.set_repeat(0, 500)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.fill((10, 10, 10))
            
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+i[6] and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, self.font_menu, punkt)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
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
                            return i[2]
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        return i[2]

            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

class Level_choose:
    def __init__(self, punkts, title):
        self.punkts = punkts
        self.title = title
        self.font_menu = pygame.font.Font('fonts/ComicTalecopy.ttf', 100)
        self.font_title = pygame.font.Font('fonts/ComicTalecopy.ttf', 150)
        self.levels = [1, 2, 3, 4, 5, 6, 7]
        self.dif_punkt = 0
        self.stage = 0
    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                if i[5] == 0:
                    surface.blit(font.render(i[2] + str(self.levels[self.stage]), 1, i[4]), (i[0], i[1]))
                else:
                    surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                if i[5] == 0:
                    surface.blit(font.render(i[2] + str(self.levels[self.stage]), 1, i[3]), (i[0], i[1]))
                else:
                    surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self, screen, window):
        done = True
        pygame.key.set_repeat(0, 500)
        pygame.mouse.set_visible(True)
        punkt = 0
        self.stage = 0
        while done:
            screen.fill((10, 10, 10))
            
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+i[6] and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, self.font_menu, punkt)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
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
                        if punkt == 1:
                            return self.stage
                        if punkt == 2:
                            return 'launch menu'
                    if e.key == pygame.K_RIGHT:
                        if punkt == 0:
                            self.stage += 1
                            if self.stage == len(self.levels):
                                self.stage = 0
                    if e.key == pygame.K_LEFT:
                        if punkt == 0:
                            self.stage -= 1
                            if self.stage == -1:
                                self.stage = len(self.levels) - 1
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if punkt == 1:
                            return self.stage
                        if punkt == 2:
                            return 'launch menu'

            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

class Mode_choose:
    def __init__(self, punkts, title):
        self.punkts = punkts
        self.title = title
        self.font_menu = pygame.font.Font('fonts/ComicTalecopy.ttf', 100)
        self.font_title = pygame.font.Font('fonts/ComicTalecopy.ttf', 150)
        self.modes = ['Standard mode', 'Bomb defusion mode', 'Endless mode']
        self.mode = 0
        self.stage = 0
    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                if i[5] == 0:
                    surface.blit(font.render(i[2] + self.modes[self.mode], 1, i[4]), (i[0], i[1]))
                else:
                    surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                if i[5] == 0:
                    surface.blit(font.render(i[2] + self.modes[self.mode], 1, i[3]), (i[0], i[1]))
                else:
                    surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self, screen, window):
        done = True
        pygame.key.set_repeat(0, 500)
        pygame.mouse.set_visible(True)
        punkt = 0
        self.stage = 0
        while done:
            screen.fill((10, 10, 10))
            
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+i[6] and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, self.font_menu, punkt)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
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
                        if punkt == 1:
                            return self.mode
                        if punkt == 2:
                            return 'launch menu'
                    if e.key == pygame.K_RIGHT:
                        if punkt == 0:
                            self.mode += 1
                            if self.mode == len(self.modes):
                                self.mode = 0
                    if e.key == pygame.K_LEFT:
                        if punkt == 0:
                            self.mode -= 1
                            if self.mode == -1:
                                self.mode = len(self.modes) - 1
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if punkt == 1:
                            return self.mode
                        if punkt == 2:
                            return 'launch menu'

            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

punkts = [
    (90, 768 - 368, u'Start game', (30, 30, 30), (252, 102, 12), 0, 450),
    (90, 768 - 268, u'Options', (30, 30, 30), (252, 102, 12), 1, 450),
    (90, 768 - 168, u'Quit game', (30, 30, 30), (252, 102, 12), 2, 450)
]

punkts1 = [
    (90, 768 - 368, u'Resume', (30, 30, 30), (252, 102, 12), 0, 450),
    (90, 768 - 268, u'Restart', (30, 30, 30), (252, 102, 12), 1, 450),
    (90, 768 - 168, u'Main menu', (30, 30, 30), (252, 102, 12), 2, 450)
]
    
punkts2 = [
    (90, 768 - 268, u'Difficulty: ', (30, 30, 30), (252, 102, 12), 0, 450),
    (90, 768 - 168, u'Back ', (30, 30, 30), (252, 102, 12), 1, 450)
]
punkts3 = [
    (1366 // 2 - 225, 250, u'Next level', (255, 255, 255), (252, 102, 12), 0, 450)
]
punkts4 = [
    (1366 // 2 - 225, 250, u'Main menu', (255, 255, 255), (252, 102, 12), 0, 450)
]
punkts5 = [
    (90, 768 - 368, u'Level: ', (30, 30, 30), (252, 102, 12), 0, 450),
    (90, 768 - 268, u'Start', (30, 30, 30), (252, 102, 12), 1, 450),
    (90, 768 - 168, u'Back', (30, 30, 30), (252, 102, 12), 2, 450)
]
punkts6 = [
    (90, 768 - 368, u'Mode: ', (30, 30, 30), (252, 102, 12), 0, 450),
    (90, 768 - 268, u'Choose', (30, 30, 30), (252, 102, 12), 1, 450),
    (90, 768 - 168, u'Back', (30, 30, 30), (252, 102, 12), 2, 450)
]