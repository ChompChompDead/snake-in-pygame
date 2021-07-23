import pygame
import sys
import random
from pygame.math import Vector2
pygame.init()

#snake class
class Snake:
    def __init__(self):
        self.movementDirection = Vector2(1, 0)
        self.snake = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.expanding = False

    def createSnake(self):
        for block in self.snake:
            xPos = int(block.x * cellSize)
            yPos = int(block.y * cellSize)
            snakeBlock = pygame.Rect(xPos, yPos, cellSize, cellSize)
            pygame.draw.rect(screen, (80,120,240), snakeBlock)

    def moveSnake(self):
        if self.expanding == True:
            snakeClone = self.snake[:]
            snakeClone.insert(0, snakeClone[0] + self.movementDirection)
            self.snake = snakeClone
            self.expanding = False
        else:
            snakeClone = self.snake[:-1]
            snakeClone.insert(0, snakeClone[0] + self.movementDirection)
            self.snake = snakeClone

    def expand(self):
        self.expanding = True

#fruit class
class Fruit:
    def __init__(self):
        self.randomize()

    def createFruit(self):
        fruitShape = pygame.Rect(int(self.position.x * cellSize), int(self.position.y * cellSize), cellSize, cellSize)
        pygame.draw.rect(screen, (255,65,20), fruitShape)

    def randomize(self):
        self.x = random.randint(0, cellAmount - 1)
        self.y = random.randint(0, cellAmount - 1)
        self.position = Vector2(self.x, self.y)
#main class
class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkFail()

    def checkCollision(self):
        if self.snake.snake[0] == self.fruit.position:
            self.fruit.randomize()
            self.snake.expand()

    def checkFail(self):
        if not 0 <= self.snake.snake[0].x < cellAmount or not 0 <= self.snake.snake[0].x < cellAmount:
            pygame.quit()
            sys.exit()
            
        for block in self.snake.snake[1:]:
            if block == self.snake.snake[0]:
                pygame.quit()
                sys.exit()
# variables
cellSize = 20
cellAmount = 20
maxFPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cellAmount * cellSize, cellAmount * cellSize))
screenUpdate = pygame.USEREVENT
pygame.time.set_timer(screenUpdate, 150)
main = Main()
# title
pygame.display.set_caption("Snake")

# updating screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screenUpdate:
            main.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if main.snake.movementDirection.y != 1:
                    main.snake.movementDirection = Vector2(0, -1)
            if event.key == pygame.K_a:
                if main.snake.movementDirection.x != 1:
                    main.snake.movementDirection = Vector2(-1, 0)
            if event.key == pygame.K_s:
                if main.snake.movementDirection.y != -1:
                    main.snake.movementDirection = Vector2(0, 1)
            if event.key == pygame.K_d:
                if main.snake.movementDirection.x != -1:
                    main.snake.movementDirection = Vector2(1, 0)

    screen.fill((90, 219, 124))
    main.fruit.createFruit()
    main.snake.createSnake()
    pygame.display.update()   
    clock.tick(maxFPS)