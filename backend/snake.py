from random import choice

# 32 x 32 board size
# 1 x 1 cell size
# 1 wall size

# 0 means empty
# 1 means wall
# 2 means snake
# 3 means fruit

def spawn_fruit(): pass
class Snake: pass

SNAKE = None
BOARD = [[0]*32 for i in range(32)]

def reset():
    global BOARD, SCORE, SNAKE
    BOARD = [[0]*32 for i in range(32)]
    SCORE = 0
    SNAKE = Snake()

# adding walls
for i in [0, 31]:
    for j in range(32):
        BOARD[i][j] = 1
for j in [0,31]:
    for i in range(32):
        BOARD[i][j] = 1

pos = set()
for i in range(1, 31):
    for j in range(1, 31):
        pos.add((i,j))

def spawn_fruit():
    global BOARD
    snake_pos = set(SNAKE.body)
    free_pos = list(pos-snake_pos)
    fruit_posi, fruit_posj = choice(free_pos)
    BOARD[fruit_posi][fruit_posj] = 3
    return (fruit_posi, fruit_posj)


FRUIT = None

SCORE = 0

class Snake:
    def __init__(self) -> None:
        global BOARD
        self.body = [(20, 20),(19,20), (18, 20), (17, 20), (16, 20)]
        self.direction = (0, 1)
        for i,j in self.body:
            BOARD[i][j] = 2
    def up(self) -> None:
        if self.direction != (1, 0):
            self.direction = (-1, 0)
    
    def down(self) -> None:
        if self.direction != (-1, 0):
            self.direction = (1, 0)

    def left(self) -> None:
        if self.direction != (0, 1):
            self.direction = (0, -1)

    def right(self) -> None:
        if self.direction != (0, -1):
            self.direction = (0, 1)

    def move(self):
        global BOARD, SCORE, FRUIT

        new_body = [0]*len(self.body)
        dr, dc = self.direction
        new_body[0] = (self.body[0][0]+dr, self.body[0][1]+dc)
        for i in range(1, len(self.body)):
            new_body[i] = self.body[i-1]
        for i in range(len(new_body)):
            for j in range(i+1, len(new_body)):
                if new_body[i] == new_body[j]:
                    SCORE -= 100
                    return 0
        for i,j in new_body:
            if BOARD[i][j] == 1:
                SCORE -= 100
                return 0
        for i,j in self.body:
            BOARD[i][j] = 0
        self.body = new_body
        for i,j in self.body:
            BOARD[i][j] = 2
        for i,j in SNAKE.body:
            if FRUIT == (i,j):
                FRUIT = spawn_fruit()
                SCORE += 1
        return 1
            

SNAKE = Snake()
FRUIT = spawn_fruit()


def game():
    movement = [SNAKE.up, SNAKE.down, SNAKE.left, SNAKE.right]
    fn = choice(movement)
    fn()
    return SNAKE.move()
