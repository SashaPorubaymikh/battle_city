import pygame
from DisplayScale import screen_width, screen_height
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.Surface((screen_width, screen_height))

done = True
clock = pygame.time.Clock()

while done:
    for e in pygame.event.get():
        if e.tpype == pygame.QUIT():
            done = False

    win.blit(screen(0, 0))
    
    clock.tick(40)
