import pygame, sys, random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (193, 144, 107), block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, (215,71,15), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit = Fruit()
            self.snake.body.append(self.snake.body[-1] + self.snake.direction)

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)

    screen.fill((107, 142, 35))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)