import pygame
import sys
import random
from pygame.math import Vector2
pygame.init()

#snake class
class Snake:
    def __init__(self):
        self.movementDirection = Vector2(1, 0)
        self.snake = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def createSnake(self):
        for block in self.snake:
            xPos = int(block.x * cellSize)
            yPos = int(block.y * cellSize)
            snakeBlock = pygame.Rect(xPos, yPos, cellSize, cellSize)
            pygame.draw.rect(screen, (80,120,240), snakeBlock)

    def moveSnake(self):
        snakeClone = self.snake[:-1]
        snakeClone.insert(0, snakeClone[0] + self.movementDirection)
        self.snake = snakeClone
#fruit class
class Fruit:
    def __init__(self):
        self.x = random.randint(0, cellAmount - 1)
        self.y = random.randint(0, cellAmount - 1)
        self.position = Vector2(self.x, self.y)

    def createFruit(self):
        fruitShape = pygame.Rect(int(self.position.x * cellSize), int(self.position.y * cellSize), cellSize, cellSize)
        pygame.draw.rect(screen, (255,65,20), fruitShape)

# variables
cellSize = 20
cellAmount = 20
maxFPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cellAmount * cellSize, cellAmount * cellSize))
screenUpdate = pygame.USEREVENT
pygame.time.set_timer(screenUpdate, 200)
fruit = Fruit()
snake = Snake()

# title
pygame.display.set_caption("Snake")

# updating screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screenUpdate:
            snake.moveSnake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.movementDirection = Vector2(0, -1)
            if event.key == pygame.K_a:
                snake.movementDirection = Vector2(-1, 0)
            if event.key == pygame.K_s:
                snake.movementDirection = Vector2(0, 1)
            if event.key == pygame.K_d:
                snake.movementDirection = Vector2(1, 0)
                
    screen.fill((90, 219, 124))
    fruit.createFruit()
    snake.createSnake()
    pygame.display.update()   
    clock.tick(maxFPS)