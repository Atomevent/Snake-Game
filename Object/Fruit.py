import random
import pygame
from Object.Constant import Green,Square_size
class fruit:
    def __init__(self,Display):
        self.Display = Display
        self.cooldownfruit = 0
        self.Posrow = 0
        self.Poscol = 0
    def generate_fruit(self):
        if self.cooldownfruit == 0:
            self.Posrow = random.randint(0,59)
            self.Poscol = random.randint(0,59)
            self.cooldownfruit = 1
        elif self.cooldownfruit > 0 and self.cooldownfruit<400:

            self.cooldownfruit += 1
        elif self.cooldownfruit >=400:

            self.cooldownfruit = 0
        pygame.draw.rect(self.Display, Green, ( (self.Poscol * (Square_size + 1)) + 1, (self.Posrow * (Square_size + 1)) + 1, Square_size, Square_size))
