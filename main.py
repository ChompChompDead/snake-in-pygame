import pygame
import sys
import random
from pygame.math import Vector2
pygame.init()

#fruit class
class Fruit:
    def __init__(self):
        self.x = random.randint(0, cellAmount - 1)
        self.y = random.randint(0, cellAmount - 1)
        self.position = Vector2(self.x, self.y)

    def createFruit(self):
        fruitShape = pygame.Rect(int(self.position.x * cellSize), int(self.position.y * cellSize), cellSize, cellSize)
        pygame.draw.rect(screen,(255,65,20), fruitShape)

# variables
cellSize = 20
cellAmount = 20
maxFPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cellAmount * cellSize, cellAmount * cellSize))
fruit = Fruit()

# title
pygame.display.set_caption("Snake")

# updating screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((90, 219, 124))
    fruit.createFruit()
    pygame.display.update()   
    clock.tick(maxFPS)