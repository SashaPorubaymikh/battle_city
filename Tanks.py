import pygame
from DisplayScale import screen_width, screen_height

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.Surface((screen_width, screen_height))

done = True
clock = pygame.time.Clock()

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.ESCAPE:
            done = False
            
    screen.fill((255, 255, 255))

    win.blit(screen, (0, 0))

    pygame.display.flip()
    
    clock.tick(40)
