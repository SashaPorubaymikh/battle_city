import sys

import pygame

from Levels import level1, level2
from Blocks import Blocks
from Player import Player
from Bullet import Bullet
from Controls import Controls
from Enemy import Enemy
from Friend import Friend
from status_bar import Status_bar
from timer import Timer
from menu import Menu, punkts, punkts1

pygame.init()
pygame.font.init()

#Создание игрового окна
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)
scr_w = infos.current_w
scr_h = infos.current_h
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.Surface((scr_w, scr_h))
full_screen = True

#Создание перснaжа
sprite_group = []
left = right = up = down = lup = ldown = lright = lleft = False
lup = True
bullets_group = []

#Персонаж, врги и друзья
enemies = friends = 0

#Создание меню
pause = Menu(punkts1)
menu = Menu(punkts)

#Создание строки состояния
status_bar = Status_bar(0, 0)

#Создание Таймера
timer = Timer()

#Создание уровня
max_enemies = 0
spavned_enemies = 0
total_enemies = 0
levels = []
stage = 0
bricks_group = []
enemy_spavner_group = []
levels.append(level1)
levels.append(level2)
level_num = 0
lvl_w = lvl_h = 0
def make_level(level_num, max_e, total_e):
    x = y = 0
    global bricks_group, sprite_group, lvl_w, lvl_h, enemies, friends, stage, max_enemies, total_enemies
    max_enemies = max_e
    total_enemies = total_e
    stage = level_num + 1
    bricks_group = []
    sprite_group = []
    enemies = friends = 0
    lvl_h = len(levels[level_num]) * 40
    for row in levels[level_num]:
        lvl_w = len(row) * 40
        for col in row:
            if col == '0':
                b1 = Blocks(x, y, 'images/blocks/brick.png', 1)
                bricks_group.append(b1)
                sprite_group.append(b1)
            if col == '1':
                b1 = Blocks(x, y, 'images/blocks/experimentalbrick.png', 1000000)
                bricks_group.append(b1)
                sprite_group.append(b1)
            if col == 'e':
                enemy_spavner_group.append([x, y])
            if col == 'f':
                sprite_group.append(Friend(x, y))
                friends += 1
            if col == 'p':
                sprite_group = [Player(x, y)] + sprite_group
                friends += 1
            x += 40
        y += 40
        x = 0
make_level(0, 6, 20)

#Создание камеры
class Camera(object):
    def __init__(self, camera_func, widht, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, widht, height )
  
    def apply(self, target):
        return target.rect.move(self.state.topleft)
  
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
  
def camera_func(camera, target_rect):
    l = -target_rect.x + scr_w/2
    t = -target_rect.y + scr_h/2
    w, h = camera.width, camera.height
 
    l = min(0, l)
    l = max(-(camera.width-scr_w), l)
    t = max(-(camera.height-scr_h), t)
    t = min(0, t)
 
    return pygame.Rect(l, t, w, h)
camera = Camera(camera_func, lvl_w, lvl_h)

#Отображениe управления
controls_list = ['Escape - exit',
                 'W, arrow up - move up',
                 'D, arrow right - move right',
                 'S, arrow down - move down',
                 'A, arrow left - move left',
                 'F - turn on/turn off fullscreen mode',
                 'Space, mouse click - shoot',
                 'C - show/hide controls list']

control = Controls(scr_w, scr_h, controls_list)
control.show()

#Конфигурации главного цикла
show_controls = False
done = True

clock = pygame.time.Clock()
if menu.menu(screen, win) == 'exit':
    sys.exit()
pygame.key.set_repeat(10, 10)

while done:
    left = right = up = down = False
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
            
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                menureturn = pause.menu(screen, win)
                if menureturn == 'exit':
                    menureturn = menu.menu(screen, win)
                    if menureturn == 'exit':
                        done = False
                    if menureturn == 'game':
                        make_level(0, 6, 20)
                pygame.key.set_repeat(10, 10)

            if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                sprite_group[0].dir = sprite_group[0].ldir = 'left'
            elif e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                sprite_group[0].dir = sprite_group[0].ldir = 'right'
            elif e.key == pygame.K_UP or e.key == pygame.K_w:
                sprite_group[0].dir = sprite_group[0].ldir = 'up'
            elif e.key == pygame.K_DOWN or e.key == pygame.K_s:
                sprite_group[0].dir = sprite_group[0].ldir = 'down'
            if e.key == pygame.K_SPACE and sprite_group[0].ready == True and sprite_group[0].isdead == False:
                sprite_group[0].shoot(bullets_group)
            # if e.key == pygame.K_1:
            #     sprite_group = [Player(720, 640), Enemy(80, 40), Enemy(1360, 40), Friend(800, 680), Friend(640, 680), Enemy(120, 90), Enemy(1260, 100)]
            #     enemy_target_list = [sprite_group[0], sprite_group[3], sprite_group[4]]
            #     friend_target_list = [sprite_group[1], sprite_group[2], sprite_group[5], sprite_group[6]]
            #     make_level(0)
            # if e.key == pygame.K_2:
            #     sprite_group = []
            #     enemy_target_list = []
            #     make_level(1)

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_c:
                if show_controls == False:
                    show_controls = True
                else:
                    show_controls = False

            if e.key == pygame.K_f:
                if full_screen == True:
                    win = pygame.display.set_mode((scr_w, scr_h))
                    full_screen = False
                else:
                    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    full_screen = True

            if e.key == pygame.K_UP or e.key == pygame.K_w:
                sprite_group[0].dir = ''
            if e.key == pygame.K_DOWN  or e.key == pygame.K_s:
                sprite_group[0].dir = ''
            if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                sprite_group[0].dir = ''
            if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                sprite_group[0].dir = ''

        if e.type == pygame.MOUSEBUTTONDOWN  and isinstance(sprite_group[0], Player) and sprite_group[0].ready == True:
            if e.button == 1:
                sprite_group[0].shoot(bullets_group)            
            
    screen.fill((5, 5, 5))
    
    #отрисовка объектов
    for i in bricks_group:
        i.update(bricks_group, sprite_group)
    for i in bricks_group:
        screen.blit(i.image, camera.apply(i))
    for i in bullets_group:
        if i.dir == 'up' or i.dir == 'down':
            screen.blit(i.image, camera.apply(i))
        else:
            screen.blit(pygame.transform.rotate(i.image, 90), camera.apply(i))

    #Обновление персонажей
    if len(sprite_group) > 0:
        camera.update(sprite_group[0])
    for i in bullets_group:
        i.update(i.dir, screen, sprite_group, bullets_group, lvl_w, lvl_h)
    for i in reversed(sprite_group):
        if isinstance(i, Enemy):
            if i.update(sprite_group, friends, enemies, bullets_group, lvl_w, lvl_h) == 0:
                enemies -= 1
            screen.blit(i.image, camera.apply(i))
        if isinstance(i, Player) and i.isdead == False:
            if i.update(sprite_group, screen, friends) == 0:
                friends -= 1
            screen.blit(i.image, camera.apply(i))
            screen.blit(i.recharge, (camera.apply(i)[0], camera.apply(i)[1] - 10))
        elif isinstance(i, Player) and i.isdead == True:
            i.rect.x = i.rect.y = -40
        if isinstance(i, Friend):
            if i.update(sprite_group, enemies, friends, bullets_group, lvl_w, lvl_h) == 0:
                friends -= 1
            screen.blit(i.image, camera.apply(i))
    if timer.update() == True and spavned_enemies < total_enemies:
        for i in enemy_spavner_group:
            if enemies < max_enemies:
                sprite_group.append(Enemy(i[0], i[1]))
                enemies += 1
                spavned_enemies += 1
    status_bar.show(sprite_group[0].lifes, friends, total_enemies - spavned_enemies, stage, screen, scr_w)

    if show_controls == True:
        win.blit(control.surface, (0, 0))

    win.blit(screen, (0, 0))
    
    pygame.display.flip()
    
    clock.tick(40)