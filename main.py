import pygame
from Object.Constant import Width , Height
from Object.grid import Grid

Display = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Snlither")

def main():
    running = True
    grid = Grid(Display)
    FPS = 60
    clock = pygame.time.Clock()
    value ="up"
    cooldown = 0
    while running:
        clock.tick(FPS)
        grid.draw_grid()
        grid.movesnake(value)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        if cooldown == 0:
            if key[pygame.K_a]:
                value = grid.rotate(value,"left")
            elif key[pygame.K_d]:
                value = grid.rotate(value,"right")
        elif cooldown >0 and cooldown <=8:
            cooldown+= 1
        else:
            cooldown=0


        pygame.display.update()
    quit()
main()