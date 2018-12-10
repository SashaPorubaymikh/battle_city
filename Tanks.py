import pygame
from DisplayScale import screen_width, screen_height
from Levels import level1
from Blocks import Blocks
from Player import Player

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.Surface((screen_width, screen_height))

levels = []
levels.append(level1)
level_num = 0
bricks_group = []
player = Player(100, 100)
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
left = right = up = down = lup = ldown = lright = lleft = False
lup = True

x = y = 0

for row in levels[level_num]:
    for col in row:
        if col == '0':
            b1 = Blocks(x, y, 'images/blocks/brick.png')
            sprite_group.add(b1)
            bricks_group.append(b1)
        x += 40
    y += 40
    x = 0


done = True
clock = pygame.time.Clock()

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            # if e.key == pygame.ESCAPE:
            #     done = False
            if e.key == pygame.K_LEFT:
                left = lleft = True
                lright = ldown = lup = up = down = right = False
            if e.key == pygame.K_RIGHT:
                right = lright = True
                lleft = left = lup = up = ldown = down = False
            if e.key == pygame.K_UP:
                up = lup = True
                lleft = left = lright = right = ldown = down = False
            if e.key == pygame.K_DOWN:
                down = ldown = True
                lup = up = right = lright = left = lleft = False
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                up = False
            if e.key == pygame.K_DOWN:
                down = False
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_RIGHT:
                right = False
            
    screen.fill((5, 5, 5))

    player.update(left, right, up, down, lleft, lright, lup, ldown, bricks_group)

    # sprite_group.draw(screen)

    for i in sprite_group:
        screen.blit(i.image, (i.rect.x, i.rect.y))

    win.blit(screen, (0, 0))

    pygame.display.flip()
    
    clock.tick(40)
