import pygame
from Levels import level1, level2
from Blocks import Blocks
from Player import Player
from Bullet import Bullet
from Controls import Controls
from Enemy import Enemy
from Friend import Friend
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
player = Player(0, 0)
left = right = up = down = lup = ldown = lright = lleft = False
lup = True
bullets_group = []

#Создание врага
enemy = Enemy(0, 0)
enemy_target_list = []

#Создание друга
friend = Friend(0, 0)
friend_target_list = []

#Создание уровня
levels = []
bricks_group = []
levels.append(level1)
levels.append(level2)
level_num = 0
lvl_w = lvl_h = 0
def make_level(level_num):
    x = y = 0
    global bricks_group, lvl_w, lvl_h
    bricks_group = []
    lvl_h = len(levels[level_num]) * 40
    for row in levels[level_num]:
        lvl_w = len(row) * 40
        for col in row:
            if col == '0':
                b1 = Blocks(x, y, 'images/blocks/brick.png', 1)
                bricks_group.append(b1)
                sprite_group.append(b1)
            if col == '1':
                b1 = Blocks(x, y, 'images/blocks/experimentalbrick.png', 10)
                bricks_group.append(b1)
                sprite_group.append(b1)
            x += 40
        y += 40
        x = 0
#sprite_group = [Player(720, 720), Enemy(40, 80), Enemy(1340, 40)]
#enemy_target_list = [sprite_group[0]]
make_level(0)

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
pygame.key.set_repeat(10, 10)

while done:
    left = right = up = down = False
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
            
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_f:
                if full_screen == True:
                    win = pygame.display.set_mode((scr_w, scr_h))
                    full_screen = False
                else:
                    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    full_screen = True
            if e.key == pygame.K_ESCAPE:
                done = False
            if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                left = lleft = True
                lright = ldown = lup = up = down = right = False
            if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                right = lright = True
                lleft = left = lup = up = ldown = down = False
            if e.key == pygame.K_UP or e.key == pygame.K_w:
                up = lup = True
                lleft = left = lright = right = ldown = down = False
            if e.key == pygame.K_DOWN or e.key == pygame.K_s:
                down = ldown = True
                lup = up = right = lright = left = lleft = False
            if e.key == pygame.K_SPACE and isinstance(sprite_group[0], Player) and sprite_group[0].ready == True:
                sprite_group[0].ready = False
                sprite_group[0].timer = 0
                if up or lup:
                    bull = Bullet(sprite_group[0].rect.x + 18, sprite_group[0].rect.y, 'images/bullets/pbullet_ver.png', 'up')
                    bullets_group.append(bull)
                if down or ldown:
                    bull = Bullet(sprite_group[0].rect.x + 18, sprite_group[0].rect.y+30, 'images/bullets/pbullet_ver.png', 'down')
                    bullets_group.append(bull)
                if left or lleft:
                    bull = Bullet(sprite_group[0].rect.x, sprite_group[0].rect.y + 18, 'images/bullets/pbullet_ver.png', 'left')
                    bullets_group.append(bull)
                if right or lright:
                    bull = Bullet(sprite_group[0].rect.x + 30, sprite_group[0].rect.y + 18, 'images/bullets/pbullet_ver.png', 'right')
                    bullets_group.append(bull)
            if e.key == pygame.K_c:
                if show_controls == False:
                    show_controls = True
                else:
                    show_controls = False
            if e.key == pygame.K_1:
                sprite_group = [Player(720, 640), Enemy(80, 40), Enemy(1360, 40), Friend(800, 680), Friend(640, 680), Enemy(120, 40), Enemy(1320, 40)]
                enemy_target_list = [sprite_group[0], sprite_group[3], sprite_group[4]]
                friend_target_list = [sprite_group[1], sprite_group[2], sprite_group[5], sprite_group[6]]
                make_level(0)
            if e.key == pygame.K_2:
                sprite_group = []
                enemy_target_list = []
                make_level(1)

        if e.type == pygame.MOUSEBUTTONDOWN  and isinstance(sprite_group[0], Player) and sprite_group[0].ready == True:
            if e.button == 1:
                sprite_group[0].ready = False
                sprite_group[0].timer = 0
                if up or lup:
                    bull = Bullet(sprite_group[0].rect.x + 18, sprite_group[0].rect.y, 'images/bullets/pbullet_ver.png', 'up')
                    bullets_group.append(bull)
                if down or ldown:
                    bull = Bullet(sprite_group[0].rect.x + 18, sprite_group[0].rect.y+30, 'images/bullets/pbullet_ver.png', 'down')
                    bullets_group.append(bull)
                if left or lleft:
                    bull = Bullet(sprite_group[0].rect.x, sprite_group[0].rect.y + 18, 'images/bullets/pbullet_ver.png', 'left')
                    bullets_group.append(bull)
                if right or lright:
                    bull = Bullet(sprite_group[0].rect.x + 30, sprite_group[0].rect.y + 18, 'images/bullets/pbullet_ver.png', 'right')
                    bullets_group.append(bull)

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP or e.key == pygame.K_w:
                up = False
            if e.key == pygame.K_DOWN  or e.key == pygame.K_s:
                down = False
            if e.key == pygame.K_LEFT or e.key == pygame.K_a:
                left = False
            if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
                right = False
            
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
    for i in sprite_group:
        if isinstance(i, Enemy):
            i.update(sprite_group, enemy_target_list, bullets_group, lvl_w, lvl_h, friend_target_list)
            screen.blit(i.image, camera.apply(i))
        if isinstance(i, Player):
            i.update(left, right, up, down, lleft, lright, lup, ldown, sprite_group, screen, enemy_target_list)
            screen.blit(i.image, camera.apply(i))
            screen.blit(i.recharge, (camera.apply(i)[0], camera.apply(i)[1] - 10))
        if isinstance(i, Friend):
            i.update(sprite_group, friend_target_list, bullets_group, lvl_w, lvl_h, enemy_target_list)
            screen.blit(i.image, camera.apply(i))
    
    

    win.blit(screen, (0, 0))
    if show_controls == True:
        win.blit(control.surface, (0, 0))

    pygame.display.flip()
    
    clock.tick(40)
