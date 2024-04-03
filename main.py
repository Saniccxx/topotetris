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
points = 0
level = 0
single_line = 100 * level
double_line = 300 * level
triple_line = 500 * level
tetris = 800 * level

types = ["I", "J", "L", "O", "S", "T", "Z"]


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
    elif type == "J":
        column = 3
        for c in range(3):
            board[1][column + c] = "J"
            if c == 0:
                board[0][column] = "J"
    elif type == "L":
        column = 3
        for c in range(3):
            board[1][column + c] = "L"
            if c == 2:
                board[0][column + c] = "J"
    elif type == "O":
        column = 4
        for c in range(2):
            board[1][column + c] = "O"
            board[0][column + c] = "O"
    elif type == "S":
        column = 3
        for c in range(3):
            if c == 0:
                board[1][column + c] = "S"
            elif c == 1:
                board[1][column + c] = "S"
                board[0][column + c] = "S"
            elif c == 2:
                board[0][column + c] = "S"
    elif type == "T":
        column = 3
        for c in range(3):
            board[1][column + c] = "T"
            if c == 1:
                board[1][column + c] = "T"
                board[0][column + c] = "T"
    elif type == "Z":
        column = 3
        for c in range(3):
            if c == 0:
                board[0][column + c] = "Z"
            elif c == 1:
                board[0][column + c] = "Z"
                board[1][column + c] = "Z"
            elif c == 2:
                board[1][column + c] = "Z"



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



def leaders(points):
    pass


spawn(board, random.choice(types))

running = True
while running:
    clock.tick(fps)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT or event.type == pygame.K_ESCAPE:
            running = False




    for row in range(rows):
        for column in range(columns):
            if board[row][column] == "I":
                pygame.draw.rect(screen, color("I"), pygame.Rect(column * tile_size, row * tile_size, tile_size, tile_size))
                # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(column * tile_size + border_thickness, row * tile_size + border_thickness, tile_size - 2 * border_thickness, tile_size - 2 * border_thickness))
            if board[row][column] == "J":
                pygame.draw.rect(screen, color("J"), pygame.Rect(column * tile_size, row * tile_size, tile_size, tile_size))
            if board[row][column] == "L":
                pygame.draw.rect(screen, color("L"), pygame.Rect(column * tile_size, row * tile_size, tile_size, tile_size))
            if board[row][column] == "O":
                pygame.draw.rect(screen, color("O"), pygame.Rect(column * tile_size, row * tile_size, tile_size, tile_size))
            if board[row][column] == "S":
                pygame.draw.rect(screen, color("S"), pygame.Rect(column * tile_size, row * tile_size, tile_size, tile_size))
            if board[row][column] == "T":
                pygame.draw.rect(screen, color("T"), pygame.Rect(column * tile_size, row * tile_size, tile_size, tile_size))
            if board[row][column] == "Z":
                pygame.draw.rect(screen, color("Z"), pygame.Rect(column * tile_size, row * tile_size, tile_size, tile_size))


    pygame.display.update()

pygame.quit()