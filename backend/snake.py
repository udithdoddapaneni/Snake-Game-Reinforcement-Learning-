from random import choice

# 32 x 32 board size
# 1 x 1 cell size
# 1 wall size

# 0 means empty
# 1 means wall
# 2 means snake
# 3 means fruit

BOARD = [[0]*32 for i in range(32)]
# adding walls
for i in [0, 31]:
    for j in range(32):
        BOARD[i][j] = 1
for j in [0,31]:
    for i in range(32):
        BOARD[i][j] = 1

class Snake:
    def __init__(self) -> None:
        global BOARD
        self.body = [(30,2),(30,1)]
        self.direction = (0, 1)
        for i,j in self.body:
            BOARD[i][j] = 2
    def up(self) -> None:
        self.direction = (-1, 0)
    
    def down(self) -> None:
        self.direction = (1, 0)

    def left(self) -> None:
        self.direction = (0, -1)

    def right(self) -> None:
        self.direction = (0, 1)

    def move(self):
        global BOARD
        new_body = [0]*len(self.body)
        dr, dc = self.direction
        new_body[0] = (self.body[0][0]+dr, self.body[0][1]+dc)
        for i in range(1, len(self.body)):
            new_body[i] = self.body[i-1]
        for i,j in self.body:
            BOARD[i][j] = 0
        self.body = new_body
        for i,j in self.body:
            BOARD[i][j] = 2

pos = set()
for i in range(1, 31):
    for j in range(1, 31):
        pos.add((i,j))

SNAKE = Snake()

def spawn_fruit():
    global BOARD
    snake_pos = set(SNAKE.body)
    free_pos = pos-snake_pos
    fruit_posi, fruit_posj = choice(free_pos)
    BOARD[fruit_posi][fruit_posj] = 3
