import pygame
import sys

pygame.init()

# variables
cellSize = 20
cellAmount = 20
maxFPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cellAmount * cellSize, cellAmount * cellSize))

# title
pygame.display.set_caption("Snake")

# updating screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((90, 219, 124))
    pygame.display.update()   
    clock.tick(maxFPS)