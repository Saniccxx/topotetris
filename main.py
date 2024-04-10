import pygame
import random
from pygame.constants import QUIT

pygame.init()
#
columns = 10
rows = 24

tile_size = 30
EMPTY = 0
BLOCK = 1
FALLING = 2
points = 0
level = 0
single_line = 100 * level
double_line = 300 * level
triple_line = 500 * level
tetris = 800 * level

let_left = True
let_right = True

types = ["I", "J", "L", "O", "S", "T", "Z"]
falls = [[False for c in range(columns)] for r in range(rows)]

screen = pygame.display.set_mode((columns * tile_size, rows * tile_size))
pygame.display.set_caption("Topotetris")
clock = pygame.time.Clock()
fps = 1
points = 0
board = [[EMPTY for c in range(columns)] for r in range(rows)]


# for i in range(1000):
#     row = random.randint(0, rows - 1)
#     column = random.randint(0, columns - 1)
#     board[row][column] = SAND

def color(type):
    if type == "I":
        return "cyan"
    elif type == "J":
        return "blue"
    elif type == "L":
        return "orange"
    elif type == "O":
        return "yellow"
    elif type == "S":
        return "lime"
    elif type == "T":
        return "purple"
    elif type == "Z":
        return "red"
# def findpos(type):
#     if type == "I":
#         return 1
#     else:
#         return 0

# def spawn(board, type):
#     if type == "I":
#         column = random.randint(0, 6)
#         for c in range(4):
#             board[21][column + c] = "I"
#     elif type == "J":
#         column = random.randint(0, 7)
#         for c in range(3):
#             board[22][column + c] = "J"
#             if c == 0:
#                 board[23][column] = "J"
#     elif type == "L":
#         column = random.randint(0, 7)
#         for c in range(3):
#             board[22][column + c] = "L"
#             if c == 2:
#                 board[23][column + c] = "J"
#     elif type == "O":
#         column = random.randint(0,8)
#         for c in range(2):
#             board[22][column + c] = "O"
#             board[23][column + c] = "O"
#     elif type == "S":
#         column = random.randint(0, 7)
#         for c in range(3):
#             board[22][column + c] = "S"
#             if c == 1:
#                 board[22][column + c] = "S"
#                 board[23][column + c] = "S"
#             elif c == 2:
#                 board[23][column + c] = "S"
#     elif type == "T":
#         column = random.randint(0, 7)
#         for c in range(3):
#             board[22][column + c] = "T"
#             if c == 1:
#                 board[22][column + c] = "T"
#                 board[23][column + c] = "T"
#     elif type == "Z":
#         column = random.randint(0, 7)
#         for c in range(3):
#             board[23][column + c] = "Z"
#             if c == 1:
#                 board[23][column + c] = "Z"
#                 board[22][column + c] = "Z"
#             elif c == 2:
#                 board[22][column + c] = "Z"
def spawn(board, type):
    if type == "I":
        column = 3
        for c in range(4):
            board[2][column + c] = "I"
            falls[2][column + c] = True
    elif type == "J":
        column = 3
        for c in range(3):
            board[1][column + c] = "J"
            falls[1][column + c] = True
            if c == 0:
                board[0][column] = "J"
                falls[0][column] = True
    elif type == "L":
        column = 3
        for c in range(3):
            board[1][column + c] = "L"
            falls[1][column + c] = True
            if c == 2:
                board[0][column + c] = "L"
                falls[0][column + c] = True
    elif type == "O":
        column = 4
        for c in range(2):
            board[1][column + c] = "O"
            board[0][column + c] = "O"
            falls[1][column + c] = True
            falls[0][column + c] = True
    elif type == "S":
        column = 3
        for c in range(3):
            if c == 0:
                board[1][column + c] = "S"
                falls[1][column + c] = True
            elif c == 1:
                board[1][column + c] = "S"
                board[0][column + c] = "S"
                falls[1][column + c] = True
                falls[0][column + c] = True
            elif c == 2:
                board[0][column + c] = "S"
                falls[0][column + c] = True
    elif type == "T":
        column = 3
        for c in range(3):
            board[1][column + c] = "T"
            falls[1][column + c] = True
            if c == 1:
                board[1][column + c] = "T"
                board[0][column + c] = "T"
                falls[1][column + c] = True
                falls[0][column + c] = True
    elif type == "Z":
        column = 3
        for c in range(3):
            if c == 0:
                board[0][column + c] = "Z"
                falls[0][column + c] = True
            elif c == 1:
                board[0][column + c] = "Z"
                board[1][column + c] = "Z"
                falls[0][column + c] = True
                falls[1][column + c] = True
            elif c == 2:
                board[1][column + c] = "Z"
                falls[1][column + c] = True




# sand = [[EMPTY for c in range(width)] for r in range(height)]
# pressed = False

def score():
    for r in range(rows):
        count = 0
        for c in range(columns):
            if board[rows - 1 - r][c] != 0:
                count += 100
            if board[rows - 1 - r][c] != 0 and board[rows - 2][c] != 0:
                count += 300
            if board[rows - 1 - r][c] != 0 and board[rows - 2][c] != 0 and board[rows - 3][c] != 0:
                count += 500


def left():
    global let_left
    temp_board = []
    if let_left:
        for r in range(rows):
            for c in range(columns):
                if falls[r][c]:
                    if c - 1 >= 0 and board[r][c - 1] == EMPTY:
                        falls[r][c - 1] = True
                        falls[r][c] = False
                        board[r][c - 1] = board[r][c]
                        board[r][c] = EMPTY
                        if c - 2 < 0:
                            let_left = False
    else:
        pass

def right():
    global let_right
    temp_falls = [[False for c in range(columns)] for r in range(rows)]
    temp_board = [[0 for c in range(columns)] for r in range(rows)]
    if let_right:
        for r in range(rows):
            for c in range(columns):
                if falls[r][c]:
                    if c + 1 < columns and board[r][c + 1] == EMPTY:
                        temp_falls[r][c + 1] = True
                        falls[r][c] = False
                        temp_board[r][c + 1] = board[r][c]
                        board[r][c] = EMPTY
                        if c + 2 >= rows:
                            let_right = False
        for r in range(rows):
            for c in range(columns):
                if temp_board[r][c] != 0:
                    board[r][c] = temp_board[r][c]
                if temp_falls[r][c]:
                    falls[r][c] = temp_falls[r][c]
    else:
        pass

def check():
    for r in range(rows):
        for c in range(columns):
            if falls[r][c]:
                return False
    return True

def leaders(points):
    pass


spawn(board, random.choice(types))

running = True
while running:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT or event.type == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left()
            elif event.key == pygame.K_RIGHT:
                right()


    row = rows - 1
    column = 0
    while True:

        if falls[row][column]:
            if row + 1 < rows and board[row + 1][column] == EMPTY:
                board[row + 1][column] = board[row][column]
                board[row][column] = EMPTY
                falls[row + 1][column] = True
                falls[row][column] = False
            else:
                falls[row][column] = False

        if check():
            spawn(board, random.choice(types))


        column += 1
        if column == columns:
            column = 0
            row -= 1
        if row < 0:
            break



    for row in range(rows):
        for column in range(columns):
            pygame.draw.rect(screen, "white",
                             pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))

            if board[row][column] == "I":
                pygame.draw.rect(screen, color("I"), pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
                # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(column * tile_size + border_thickness, row * tile_size + border_thickness, tile_size - 2 * border_thickness, tile_size - 2 * border_thickness))
            if board[row][column] == "J":
                pygame.draw.rect(screen, color("J"), pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "L":
                pygame.draw.rect(screen, color("L"), pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "O":
                pygame.draw.rect(screen, color("O"), pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "S":
                pygame.draw.rect(screen, color("S"), pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "T":
                pygame.draw.rect(screen, color("T"), pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "Z":
                pygame.draw.rect(screen, color("Z"), pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))


    pygame.display.update()
#end
pygame.quit()