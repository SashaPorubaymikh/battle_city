import pygame
from DisplayScale import screen_width, screen_height
from Characters import Player
from Blocks import Block
from Levels import level1

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.Surface((screen_width, screen_height))

sprite_group = pygame.sprite.Group()
bricks_group = []

x = y = 0
for row in level1:
    for col in row:
        if col == '0':
            b1 = Block(x, y, 'images/blocks/brick.png')
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

    win.blit(screen, (0, 0))
    
    clock.tick(40)
