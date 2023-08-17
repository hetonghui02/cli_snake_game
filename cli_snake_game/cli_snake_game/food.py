import random

class Food:
    def __init__(self):
        self.position = (random.randint(0, 20), random.randint(0, 20))

    def generate(self):
        self.position = (random.randint(0, 20), random.randint(0, 20))
