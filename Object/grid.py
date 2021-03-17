import pygame
from Object.Constant import White,Black,Row,Col,Square_size
from Object.snake import snake
from Object.Fruit import fruit
class Grid:
    def __init__(self,Display):
        self.Display = Display
        self.snake = snake(Display)
        self.snake.start_snake()
        self.fruit = fruit(Display)
        self.cooldownrotate = 0
    def draw_grid(self):
        self.Display.fill(Black)
        for row in range(Row):
            for col in range(Col):
                pygame.draw.rect(self.Display,White,((col*(Square_size+1))+1,(row*(Square_size+1))+1,Square_size,Square_size))
        self.snake.draw_snake()

    def rotate(self,Value,Where):
        if self.cooldownrotate == 0:
            if Where == "right":
                if Value == "up":
                    self.cooldownrotate = 1
                    return "right"
                elif Value == "left":
                    self.cooldownrotate = 1
                    return "up"
                elif Value == "right":
                    self.cooldownrotate = 1
                    return "down"
                elif Value == "down":
                    self.cooldownrotate = 1
                    return "left"
            if Where == "left":
                if Value == "up":
                    self.cooldownrotate = 1
                    return "left"
                elif Value == "left":
                    self.cooldownrotate = 1
                    return "down"
                elif Value == "right":
                    self.cooldownrotate = 1
                    return "up"
                elif Value == "down":
                    self.cooldownrotate = 1
                    return "right"

        elif self.cooldownrotate >0 and self.cooldownrotate <10:
            self.cooldownrotate+=1
            return Value
        elif self.cooldownrotate >= 10:
            self.cooldownrotate = 0
            return Value

    def movesnake(self,Value):
        self.snake.move(Value)




