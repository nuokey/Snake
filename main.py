import pygame
from random import randint as rnd

class Snake():
    def __init__(self):
        self.body = [[90, 50], [70, 50], [50, 50]]
        self.texture = pygame.image.load('snake.png')
        self.direction = [1, 0]

    def draw(self):
        for i in self.body:
            screen.blit(self.texture, (i[0], i[1]))

    def move(self):
        for i in range(len(self.body) -1 , -1, -1):
            if i == 0:
                self.body[i][0] += self.direction[0] * 10
                self.body[i][1] += self.direction[1] * 10
            else:
                self.body[i][0] = self.body[i-1][0]
                self.body[i][1] = self.body[i-1][1]

    def exit_check(self):
        if self.body[0][0] > size[0]:
            self.body[0][0] = -20
        if self.body[0][0] < -20:
            self.body[0][0] = size[0]

        if self.body[0][1] > size[1]:
            self.body[0][1] = -20
        if self.body[0][1] < -20:
            self.body[0][1] = size[1]

    def body_check(self):
        for i in range(2, len(self.body)):
            try:
                x = abs(self.body[i][0] - self.body[0][0])
                y = abs(self.body[i][1] - self.body[0][1])
                if x < 10 and y < 10:
                    del self.body[i:len(self.body)-1]
            except:
                pass

    def update(self):
        self.move()
        self.exit_check()
        self.body_check()

class Apple():
    def __init__(self):
        self.texture = pygame.image.load('apple.png')
        self.create()

    def create(self):
        self.x = rnd(0, size[0] - 40)
        self.y = rnd(0, size[1] - 40)

    def collide(self):
        if abs(self.x - snake.body[0][0]) <= 30 and abs(self.y - snake.body[0][1]) <= 30:
            self.create()
            snake.body.append([self.x, self.y])

    def draw(self):
        screen.blit(self.texture, (self.x, self.y))

size = (1280, 720)
snake = Snake()
apple = Apple()

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake | by NuoKey')
pygame.init()
clock = pygame.time.Clock()
done = False
while not done:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if snake.direction != [0, 1]:
                    snake.direction = [0, -1]

            if event.key == pygame.K_s:
                if snake.direction != [0, -1]:
                    snake.direction = [0, 1]

            if event.key == pygame.K_a:
                if snake.direction != [1, 0]:
                    snake.direction = [-1, 0]

            if event.key == pygame.K_d:
                if snake.direction != [-1, 0]:
                    snake.direction = [1, 0]

    snake.update()
    snake.draw()
    apple.collide()
    apple.draw()

    pygame.display.flip()
pygame.quit()