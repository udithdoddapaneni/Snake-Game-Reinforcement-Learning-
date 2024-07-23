import pygame as pg
import backend.snake as sn

pg.init()
screen = pg.display.set_mode((20*32, 20*32))
font = pg.font.SysFont('didot.ttc', 60)

objects = {0: "white", 1: "black", 2: "orange", 3: "red"}

WIDTH = 20
HEIGHT = 20


def CreateCell(x,y):

    return pg.Rect(x,y, WIDTH, HEIGHT)

def make_grid(grid):

    display_grid = [[0]*len(grid[0]) for i in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid)):
            display_grid[i][j] = CreateCell(i*WIDTH, j*WIDTH)

    return display_grid

def draw(surface, display_grid, BOARD):

    for i in range(len(BOARD)):
        for j in range(len(BOARD)):
            R = display_grid[i][j]
            pg.draw.rect(surface,objects[BOARD[i][j]], R)
#button = pg.Rect()

# environment

display_grid = make_grid(sn.BOARD)

# seeding


def simulate():
    global screen, display_grid

    FPS = 4
    start = False
    running = True
    clock = pg.time.Clock()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        val = sn.game()
        if val == 0:
            running = False
        draw(screen, display_grid, sn.BOARD)
        pg.display.update()

        clock.tick(FPS)

    pg.quit()

simulate()
