import pygame
from DisplayScale import screen_width, screen_height
from Levels import level1
from Blocks import Blocks

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.Surface((screen_width, screen_height))

levels = []
levels.append(level1)
level_num = 0
bricks_group = []
sprite_group = pygame.sprite.Group()

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
        if e.key == pygame.ESCAPE:
            done = False

    
    #sprite_group.draw(screen)
            
    screen.fill((5, 5, 5))

    for i in sprite_group:
        screen.blit(i.image, (i.x, i.y))

    win.blit(screen, (0, 0))

    pygame.display.flip()
    
    clock.tick(40)
