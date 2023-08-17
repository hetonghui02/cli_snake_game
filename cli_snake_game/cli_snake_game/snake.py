import random

class Snake:
    def __init__(self):
        self.body = [(10, 10)]
        self.direction = "UP"

    def move(self):
        head = self.body[0]
        if self.direction == "UP":
            self.body.insert(0, (head[0], head[1] - 1))
        elif self.direction == "DOWN":
            self.body.insert(0, (head[0], head[1] + 1))
        elif self.direction == "LEFT":
            self.body.insert(0, (head[0] - 1, head[1]))
        elif self.direction == "RIGHT":
            self.body.insert(0, (head[0] + 1, head[1]))
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        return self.body[0] in self.body[1:]

class Food:
    def __init__(self):
        self.position = (random.randint(0, 20), random.randint(0, 20))

    def generate(self):
        self.position = (random.randint(0, 20), random.randint(0, 20))
