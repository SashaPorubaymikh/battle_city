import pygame
from Levels import level1, level2
from Blocks import Blocks
from Player import Player
from Bullet import Bullet
pygame.init()

#Создание игрового окна
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)
scr_w = infos.current_w
scr_h = infos.current_h
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.Surface((scr_w, scr_h))
full_screen = True

#Создание персножа
player = Player(100, 100)
left = right = up = down = lup = ldown = lright = lleft = False
lup = True
bullets_group = []


#Создание уровня
levels = []
bricks_group = []
levels.append(level1)
levels.append(level2)
level_num = 0
def make_level(level_num, xx, yy):
    x = y = 0
    global bricks_group
    bricks_group = []
    for row in levels[level_num]:
        for col in row:
            if col == '0':
                b1 = Blocks(x, y, 'images/blocks/brick.png', 1)
                bricks_group.append(b1)
            x += 40
        y += 40
        x = 0
    player.rect.x = xx
    player.rect.y = yy
make_level(0, 100, 100)

#Конфигурации главного цикла
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
            if e.key == pygame.K_SPACE and player.ready == True and len(bullets_group)<5:
                player.ready = False
                player.timer = 0
                if up or lup:
                    bull = Bullet(player.rect.x + 18, player.rect.y+10, 'images/bullets/pbullet_ver.png', 'up')
                    bullets_group.append(bull)
                if down or ldown:
                    bull = Bullet(player.rect.x + 18, player.rect.y+40, 'images/bullets/pbullet_ver.png', 'down')
                    bullets_group.append(bull)
                if left or lleft:
                    bull = Bullet(player.rect.x - 10, player.rect.y + 18, 'images/bullets/pbullet_ver.png', 'left')
                    bullets_group.append(bull)
                if right or lright:
                    bull = Bullet(player.rect.x + 40, player.rect.y + 18, 'images/bullets/pbullet_ver.png', 'right')
                    bullets_group.append(bull)
            if e.key == pygame.K_1:
                make_level(0, 100, 100)
            if e.key == pygame.K_2:
                make_level(1, 40, 40)

        if e.type == pygame.MOUSEBUTTONDOWN and player.ready == True and len(bullets_group)<5:
            player.ready = False
            player.timer = 0
            if up or lup:
                bull = Bullet(player.rect.x + 18, player.rect.y+10, 'images/bullets/pbullet_ver.png', 'up')
                bullets_group.append(bull)
            if down or ldown:
                bull = Bullet(player.rect.x + 18, player.rect.y+40, 'images/bullets/pbullet_ver.png', 'down')
                bullets_group.append(bull)
            if left or lleft:
                bull = Bullet(player.rect.x - 10, player.rect.y + 18, 'images/bullets/pbullet_ver.png', 'left')
                bullets_group.append(bull)
            if right or lright:
                bull = Bullet(player.rect.x + 40, player.rect.y + 18, 'images/bullets/pbullet_ver.png', 'right')
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

    player.update(left, right, up, down, lleft, lright, lup, ldown, bricks_group, screen)

    #отрисовка объектов
    for i in bricks_group:
        i.update(bricks_group)
    for i in bricks_group:
        screen.blit(i.image, (i.rect.x, i.rect.y))
    for i in bullets_group:
        i.update(i.dir, screen, bricks_group, bullets_group, scr_w, scr_h)
    screen.blit(player.image, (player.rect.x, player.rect.y))

    win.blit(screen, (0, 0))

    pygame.display.flip()
    
    clock.tick(40)
