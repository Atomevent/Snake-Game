import pygame
from Object.Constant import Blue,Cyan,Square_size,White
from Object.Fruit import fruit

class snake:
    def __init__(self,Display):
        self.Pos_snakeb = []  # start 50,29
        self.Display = Display
        self.Cooldown = 0
        self.Cooldown2 = 0
        self.Timer2 = 10
        self.Timer = 5
        self.fruit = fruit(Display)
    def collision(self,snake,obj2):
        self.Pos_Head_col = snake[0][1]
        self.Pos_Head_row = snake[0][0]
        self.Pos_obj_col = obj2.Poscol
        self.Pos_obj_row = obj2.Posrow
        if self.Pos_Head_col == self.Pos_obj_col and self.Pos_Head_row == self.Pos_obj_row:
            obj2.Poscol = -1
            obj2.Posrow = -1
            return True
        else:
            return False
    def add_snake(self):
        if self.collision(self.Pos_snakeb,self.fruit):
            pygame.draw.rect(self.Display, White, ((self.fruit.Poscol * (Square_size + 1)) + 1, (self.fruit.Posrow * (Square_size + 1)) + 1, Square_size, Square_size))
            for i in range(len(self.Pos_snakeb)):
                self.diff_row = self.Pos_snakeb[-2][0] -self.Pos_snakeb[-1][0]
                self.diff_col = self.Pos_snakeb[-2][1] - self.Pos_snakeb[-1][1]
                if self.diff_row == 0:
                    if self.diff_col >= 1:#Right
                        self.Pos_snakeb.append([self.Pos_snakeb[-1][0],self.Pos_snakeb[-1][1]-1])
                        break
                    else:
                        self.Pos_snakeb.append([self.Pos_snakeb[-1][0], self.Pos_snakeb[-1][1] + 1])
                        break
                elif self.diff_col ==0:
                    if self.diff_row >= 1:  # Down
                        self.Pos_snakeb.append([self.Pos_snakeb[-1][0]-1, self.Pos_snakeb[-1][1] ])
                        break
                    else:
                        self.Pos_snakeb.append([self.Pos_snakeb[-1][0]+1, self.Pos_snakeb[-1][1] ])
                        break
    def start_snake(self):
            for i in range(3):
                self.Pos_snakeb.append([50, i + 29])
    def draw_snake(self):
        self.add_snake()
        self.fruit.generate_fruit()
        if  self.Pos_snakeb:
                for i in range(len(self.Pos_snakeb)):
                    self.row = self.Pos_snakeb[i][0]
                    self.col = self.Pos_snakeb[i][1]
                    if i != 0:
                        pygame.draw.rect(self.Display, Cyan, ((self.col * (Square_size + 1)) + 1, (self.row * (Square_size + 1)) + 1, Square_size, Square_size))
                pygame.draw.rect(self.Display, Blue, ((self.Pos_snakeb[0][1] * (Square_size + 1)) + 1, (self.Pos_snakeb[0][0] * (Square_size + 1)) + 1, Square_size, Square_size))
        if self.Cooldown >0 and self.Cooldown<self.Timer:
            self.Cooldown+=1
        elif self.Cooldown>=self.Timer:
            self.Cooldown = 0




    def move(self,Value):
        if self.Cooldown ==0:
            self.row1 = self.Pos_snakeb[0][0]
            self.col1 = self.Pos_snakeb[0][1]
            if Value == "up":
                if self.row1 !=0:
                    self.operate = True
            elif Value == "left":
                if self.col1 != 0:
                    self.operate = True
            elif Value == "down":
                if self.row1 !=59:
                    self.operate = True
            elif Value == "right":
                if self.col1 != 59:
                    self.operate = True
            if self.operate:
                for i in range(len(self.Pos_snakeb)):
                    if i < len(self.Pos_snakeb)-1:
                        self.Pos_snakeb[len(self.Pos_snakeb)-1-i][0] = self.Pos_snakeb[len(self.Pos_snakeb)-2-i][0]
                        self.Pos_snakeb[len(self.Pos_snakeb)-1-i][1] =self.Pos_snakeb[len(self.Pos_snakeb)-2-i][1]
                if Value == "up":
                        self.Pos_snakeb[0][0]-=1
                elif Value == "left":

                        self.Pos_snakeb[0][1] -= 1
                elif Value == "down":

                        self.Pos_snakeb[0][0] +=1
                elif Value == "right":
                        self.Pos_snakeb[0][1]+=1
                self.operate = False
                self.Cooldown = 1


