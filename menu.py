import pygame, sys

pygame.init()
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)
scr_h = infos.current_h
scr_w = infos.current_w

class Menu:
    def __init__(self):
        self.all_punkts = [
            [(90, 768 - 368, u'Start game', (30, 30, 30), (252, 102, 12), 0, 450),
            (90, 768 - 268, u'Options', (30, 30, 30), (252, 102, 12), 1, 450),
            (90, 768 - 168, u'Quit game', (30, 30, 30), (252, 102, 12), 2, 450)],
            [(90, 768 - 368, u'Resume', (30, 30, 30), (252, 102, 12), 0, 450),
            (90, 768 - 268, u'Restart', (30, 30, 30), (252, 102, 12), 1, 450),
            (90, 768 - 168, u'Main menu', (30, 30, 30), (252, 102, 12), 2, 450)],
            [(90, 768 - 468, u'Standard mode', (30, 30, 30), (252, 102, 12), 0, 450),
            (90, 768 - 368, u'Bomb defuse mode', (30, 30, 30), (252, 102, 12), 1, 450),
            (90, 768 - 268, u'Endless mode', (30, 30, 30), (252, 102, 12), 2, 450),
            (90, 768 - 168, u'Back ', (30, 30, 30), (252, 102, 12), 3, 450)],
            [(90, 768 - 268, u'Level: ', (30, 30, 30), (252, 102, 12), 0, 450),
            (90, 768 - 168, u'Back ', (30, 30, 30), (252, 102, 12), 1, 450)],
            [(1366 // 2 - 225, 250, u'Next level', (255, 255, 255), (252, 102, 12), 0, 450)],
            [(1366 // 2 - 225, 250, u'Main menu', (255, 255, 255), (252, 102, 12), 0, 450)],
        ]
        self.punkts = None
        self.titles = ['Main menu', 'Pause', 'Mode selection', 'Level selection']
        self.title = None
        self.font_menu = pygame.font.Font('fonts/ComicTalecopy.ttf', 100)
        self.font_title = pygame.font.Font('fonts/ComicTalecopy.ttf', 150)

    def render(self, surface, font, num_punkt, level=0):
        for i in self.punkts:
            if  self.punkts == self.all_punkts[3]:
                if num_punkt == i[5]:
                    surface.blit(font.render(i[2] + str(level + 1), 1, i[4]), (i[0], i[1]))
                else:
                    surface.blit(font.render(i[2] + str(level + 1), 1, i[3]), (i[0], i[1]))
            else:
                if num_punkt == i[5]:
                    surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
                else:
                    surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def main_menu(self, screen, window):
        done = True
        pygame.key.set_repeat(1, 300)
        pygame.mouse.set_visible(True)
        punkt = 0
        self.punkts = self.all_punkts[0]
        self.title = self.titles[0]
        while done:
            screen.fill((10, 10, 10))
            self.render(screen, self.font_menu, punkt)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
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
                            mode_n_level = self.start_game(screen, window)
                            if mode_n_level != None:
                                return mode_n_level
                                pygame.key.set_repeat(10, 10)
                        if punkt == 1:
                            pass
                        if punkt == 2:
                            sys.exit()

            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

        pygame.key.set_repeat(1, 1)
        pygame.mouse.set_visible(False)

    def pause(self, screen, window):
        pygame.key.set_repeat(1, 300)
        pygame.mouse.set_visible(True)
        self.punkts = self.all_punkts[1]
        punkt = 0
        self.title = self.titles[1]
        done = True
        while done:
            screen.fill((10, 10, 10))
            self.render(screen, self.font_menu, punkt)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
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
                        if punkt == 1:
                            return 'RESTART'
                            pygame.key.set_repeat(10, 10)
                        if punkt == 2:
                            return 'MAIN_MENU'
                            pygame.key.set_repeat(10, 10)
            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

        pygame.key.set_repeat(1, 1)
        pygame.mouse.set_visible(False)
    
    def start_game(self, screen, window):
        pygame.key.set_repeat(1, 300)
        pygame.mouse.set_visible(True)
        self.punkts = self.all_punkts[2]
        punkt = 0
        self.title = self.titles[2]
        done = True
        while done:
            screen.fill((10, 10, 10))
            self.render(screen, self.font_menu, punkt)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
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
                            level = self.level_selection(screen, window)
                            if level != None:
                                return {'mode' : 'ST_Mode', 'level' : level}
                            else:
                                done = False
                        if punkt == 1:
                            level = self.level_selection(screen, window)
                            if level != None:
                                return {'mode' : 'BD_Mode', 'level' : level}
                            else:
                                done = False
                        if punkt == 2:
                            level = self.level_selection(screen, window)
                            if level != None:
                                return {'mode' : 'EL_Mode', 'level' : level}
                            else:
                                done = False
                        if punkt == 3:
                            done = False
            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

        pygame.key.set_repeat(1, 1)
        pygame.mouse.set_visible(False)

    def level_selection(self, screen, window):
        pygame.key.set_repeat(1, 300)
        pygame.mouse.set_visible(True)
        self.punkts = self.all_punkts[3]
        punkt = 0
        self.title = self.titles[3]
        done = True
        level = 0
        while done:
            screen.fill((10, 10, 10))
            self.render(screen, self.font_menu, punkt, level)
            screen.blit(self.font_title.render(self.title, 1, (255, 255, 255)), (1366 // 2 - self.font_title.size(self.title)[0] // 2, 100))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
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
                    if e.key == pygame.K_RIGHT and punkt == 0:
                        level += 1
                        if level == 7:
                            level = 0
                    if e.key == pygame.K_LEFT and punkt == 0:
                        level -= 1
                        if level == -1:
                            level = 6
                    if e.key == pygame.K_KP_ENTER or e.key == pygame.K_RETURN:
                        if punkt == 0:
                            return level
                        if punkt == 1:
                            done = False
            window.blit(pygame.transform.scale(screen, (scr_w, scr_h)), (0, 0))
            pygame.display.flip()

        pygame.key.set_repeat(1, 1)
        pygame.mouse.set_visible(False)
    