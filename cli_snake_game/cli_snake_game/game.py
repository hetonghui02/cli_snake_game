import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.snake = Snake()
        self.food = Food()

    def start_game(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.direction = "UP"
                    elif event.key == pygame.K_DOWN:
                        self.snake.direction = "DOWN"
                    elif event.key == pygame.K_LEFT:
                        self.snake.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT:
                        self.snake.direction = "RIGHT"

            self.snake.move()
            self.check_collision()
            self.update_game()
            self.draw_game()

    def end_game(self):
        pygame.quit()

    def check_collision(self):
        if self.snake.body[0] == self.food.position:
            self.score += 1
            self.snake.grow()
            self.food.generate()
        elif self.snake.body[0] in self.snake.body[1:]:
            self.game_over = True
        elif self.snake.body[0][0] < 0 or self.snake.body[0][0] > 20 or self.snake.body[0][1] < 0 or self.snake.body[0][1] > 20:
            self.game_over = True

    def update_game(self):
        pygame.time.delay(100)

    def draw_game(self):
        for i in range(21):
            for j in range(21):
                if (i, j) in self.snake.body:
                    print("S", end="")
                elif (i, j) == self.food.position:
                    print("F", end="")
                else:
                    print(".", end="")
            print()
        print(f"Score: {self.score}")
