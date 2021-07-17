import pygame
import sys

pygame.init()

# variables
maxFPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

# updating screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((90, 219, 124))
    pygame.display.update()   
    clock.tick(maxFPS)     