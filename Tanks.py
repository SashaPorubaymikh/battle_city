import pygame
from DisplayScale import screen_width, screen_height

done = True
clock = pygame.time.Clock()

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.ESCAPE:
            done = False

    for i in sprite_group:
        screen.blit(i.bitmap, (i.x, i.y))
    screen.fill((150, 150, 150))

    win.blit(screen, (0, 0))
    
    clock.tick(40)
