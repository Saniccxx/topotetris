# -------------------Topotetris-------------------

# Fizyka spadania, fizyka przemieszczania, wyświetlanie, klocki - Oleksandr Shevchenko
#
# podliczanie punktów, database - Olga Zyntek


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
level = 1
cleared_lines = 0
single_line = 50
double_line = 150
triple_line = 300
tetris_line = 600
touched = False
current = None
let_left = True
let_right = True

types = ["I", "J", "L", "O", "S", "T", "Z"]
falls = [[False for c in range(columns)] for r in range(rows)]

screen_width = columns * tile_size + 200
screen_height = rows * tile_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Topotetris")
clock = pygame.time.Clock()
fps = 2
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
    elif type == "B":
        return "brown"


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
    elif type == "B":
        column = 4
        for c in range(4):
            board[1 + c][column] = "B"
            falls[1 + c][column] = True


# sand = [[EMPTY for c in range(width)] for r in range(height)]
# pressed = False
set()
spawn(board, current)
font = pygame.font.SysFont(None, 48)
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


# def left():
#     for r in range(rows):
#         for c in range(columns):
#             if falls[r][c]:
#                 if c - 1 >= 0 and board[r][c - 1] == EMPTY:
#                     # if c - 1 < 0 or board[r+1][c - 1] != EMPTY or board[r - 1][c - 1] != EMPTY:
#                     #     return
#                     if c - 1 > 0:
#                         if board[r + 1][c - 1] != EMPTY and c - 2 < 0:
#                             return
#                         if board[r + 1][c - 2] != EMPTY and c - 3 < 0:
#                             return
#                         if board[r - 1][c - 1] != EMPTY and c - 2 < 0:
#                             return
#                         if board[r - 1][c - 2] != EMPTY and c - 3 < 0:
#                             return
#                     falls[r][c - 1] = True
#                     falls[r][c] = False
#                     board[r][c - 1] = board[r][c]
#                     board[r][c] = EMPTY
# def left():
#     for r in range(rows):
#         for c in range(columns):
#             if falls[r][c]:
#                 if c - 1 >= 0 and board[r + 1][c - 1] == EMPTY:
#                     print(1)
#                     for r in range(rows):
#                         for c in range(columns):
#                             if falls[r][c]:
#                                 falls[r][c - 1] = falls[r][c]
#                                 falls[r][c] = False
#                                 board[r][c - 1] = board[r][c]
#                                 board[r][c] = EMPTY
#                     return
#                 elif c - 3 >= 0 and board[r + 1][c - 2] != EMPTY:
#                     print(2)
#                     for r in range(rows):
#                         for c in range(columns):
#                             if falls[r][c]:
#                                 falls[r][c - 1] = falls[r][c]
#                                 falls[r][c] = False
#                                 board[r][c - 1] = board[r][c]
#                                 board[r][c] = EMPTY
#                     return
#                 elif c - 2 >= 0 and board[r + 1][c - 1] != EMPTY:
#                     print(3)
#                     for r in range(rows):
#                         for c in range(columns):
#                             if falls[r][c]:
#                                 falls[r][c - 1] = falls[r][c]
#                                 falls[r][c] = False
#                                 board[r][c - 1] = board[r][c]
#                                 board[r][c] = EMPTY
#                     return
#                 else:
#                     return


# def right():
#     temp_falls = [[False for _ in range(columns)] for _ in range(rows)]
#     temp_board = [[EMPTY for _ in range(columns)] for _ in range(rows)]
#     last = len(board[0]) - 1
#     for r in range(rows):
#         for c in range(columns):
#             var = last - c
#             if falls[r][var]:
#                 # print(var)
#                 if var + 1 < columns and board[r + 1][var + 1] == EMPTY:
#                     print(1)
#                     for r in range(rows):
#                         for c in range(columns):
#                             var = last - c
#                             if falls[r][var]:
#                                 temp_falls[r][var + 1] = falls[r][var]
#                                 temp_board[r][var + 1] = board[r][var]
#                                 for r in range(rows):
#                                     for c in range(columns):
#                                         if temp_falls[r][c]:
#                                             falls[r][c] = temp_falls[r][c]
#                                             falls[r][c - 1] = False
#                                             board[r][c] = temp_board[r][c]
#                                             board[r][c - 1] = EMPTY
#
#
#
#                     return
#                 elif var + 3 < columns and board[r + 1][var + 2] != EMPTY:
#                     print(2)
#                     for r in range(rows):
#                         for c in range(columns):
#                             if falls[r][var]:
#                                 temp_falls[r][var + 1] = falls[r][var]
#                                 temp_board[r][var + 1] = board[r][var]
#                                 for r in range(rows):
#                                     for c in range(columns):
#                                         if temp_falls[r][c]:
#                                             falls[r][c] = temp_falls[r][c]
#                                             falls[r][c - 1] = False
#                                             board[r][c] = temp_board[r][c]
#                                             board[r][c - 1] = EMPTY
#                     return
#                 elif var + 2 < columns and board[r + 1][var + 1] != EMPTY:
#                     print(3)
#                     for r in range(rows):
#                         for c in range(columns):
#                             if falls[r][var]:
#                                 temp_falls[r][var + 1] = falls[r][var]
#                                 temp_board[r][var + 1] = board[r][var]
#                                 for r in range(rows):
#                                     for c in range(columns):
#                                         if temp_falls[r][c]:
#                                             falls[r][c] = temp_falls[r][c]
#                                             falls[r][c - 1] = False
#                                             board[r][c] = temp_board[r][c]
#                                             board[r][c - 1] = EMPTY
#                     return
#                 else:
#                     return



def move_right():
    temp_falls = [[False for _ in range(columns)] for _ in range(rows)]
    temp_board = [[EMPTY for _ in range(columns)] for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            if falls[r][c] and c + 1 < columns:
                if board[r][c + 1] != EMPTY:
                    if falls[r][c + 1]:
                        temp_falls[r][c + 1] = True
                        # falls[r][c] = False
                        temp_board[r][c + 1] = board[r][c]
                        # board[r][c] = EMPTY
                    else:
                        return
                else:
                    temp_falls[r][c + 1] = True
                    # falls[r][c] = False
                    temp_board[r][c + 1] = board[r][c]
                    # board[r][c] = EMPTY
    for r in range(rows):
        for c in range(columns):
            if falls[r][c]:
                falls[r][c] = False
                board[r][c] = EMPTY

    for rr in range(rows):
        for cc in range(columns):
            if temp_falls[rr][cc]:
                falls[rr][cc] = temp_falls[rr][cc]
                board[rr][cc] = temp_board[rr][cc]

def check_right():
    max_c = 0
    for r in range(rows):
        for c in range(columns):
            if falls[r][c]:
                if c > max_c:
                    max_c = c
    print(max_c)
    return max_c
def right():
    if check_right() + 1 >= columns:
        return
    else:
        move_right()

def move_left():
    temp_falls = [[False for _ in range(columns)] for _ in range(rows)]
    temp_board = [[EMPTY for _ in range(columns)] for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            if falls[r][c] and c - 1 >= 0:
                if board[r][c - 1] != EMPTY:
                    if falls[r][c - 1]:
                        temp_falls[r][c - 1] = True
                        # falls[r][c] = False
                        temp_board[r][c - 1] = board[r][c]
                        # board[r][c] = EMPTY
                    else:
                        return
                else:
                    temp_falls[r][c - 1] = True
                    # falls[r][c] = False
                    temp_board[r][c - 1] = board[r][c]
                    # board[r][c] = EMPTY
    for r in range(rows):
        for c in range(columns):
            if falls[r][c]:
                falls[r][c] = False
                board[r][c] = EMPTY

    for rr in range(rows):
        for cc in range(columns):
            if temp_falls[rr][cc]:
                falls[rr][cc] = temp_falls[rr][cc]
                board[rr][cc] = temp_board[rr][cc]

def check_left():
    min_c = 9999
    for r in range(rows):
        for c in range(columns):
            if falls[r][c]:
                if c < min_c:
                    min_c = c
    print(min_c)
    return min_c
def left():
    if check_left() - 1 < 0:
        return
    else:
        print('aaaaaaaa')
        move_left()



def set():
    global current
    current = random.choice(types)

def check():
    for r in range(rows):
        for c in range(columns):
            if falls[r][c]:
                return False
    return True

def leaders(points):
    pass

# def dol(r):
#     global board, falls
#     while r < rows:
#         for c in range(columns):
#             if falls[r][c]:
#                 if falls[r + 1][c] or falls[r + 1][c + 1] or falls[r + 1][c - 1] or board[r + 1][c] == EMPTY:
#                     dol(r + 1)
#                 else:
#                     return 1
#     return 0
# def dol(r):
#     global board, falls
#     for c in range(columns):
#         if falls[r][c]:
#             if falls[r + 1][c] or falls[r + 1][c + 1] or falls[r + 1][c - 1] or board[r + 1][c] == EMPTY:
#
#             else:
#                 return 1
#     return 0



def printer(lista):
    for r in range(len(lista)):
        print()
        for c in range(len(lista[0])):
            print(lista[r][c], end=" ")
def extract_subarray():
    global rotate_x, rotate_y
    rotate_x = 0
    rotate_y = 0
    rowsy = [i for i in range(len(falls)) if any(falls[i])]
    cols = [i for i in range(len(falls[0])) if any(row[i] for row in falls)]
    rotate_x = cols[0]
    rotate_y = rowsy[0]
    subarray = [[falls[r][c] for c in cols] for r in rowsy]
    return subarray


def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def paste():
    global board, falls
    temp_board = [[EMPTY for _ in range(columns)] for _ in range(rows)]
    final_falls = [[False for _ in range(columns)] for _ in range(rows)]
    backup_board = board
    # printer(backup_board)
    backup_falls = falls
    temp = extract_subarray()
    # current = random.choice(types)

    temp_falls = [[False for _ in range(columns)] for _ in range(rows)]
    # printer(rotate_matrix(extract_subarray()))

    while len(temp) != len(temp[0]):
        if len(temp) > len(temp[0]):
            for r in range(len(temp)):
                temp[r].append(False)
        else:
            temp.append([False for _ in range(len(temp[0]))])

    # printer(temp)
    new = rotate_matrix(temp)
    count_new = 0
    for r in range(len(new)):
        for c in range(len(new[0])):
            if new[r][c]:
                count_new += 1
    print("COUNTNEW:", count_new)
    print(new)
    for r in range(rotate_y, len(new) + rotate_y):
        for c in range(rotate_x, len(new[0]) + rotate_x):
            try:
                temp_falls[r][c] = new[r - rotate_y][c - rotate_x]
            except:
                print(1)
                return
            if current == "I":
                try:
                    temp_falls[r][c] = new[r - rotate_y - 4][c - rotate_x]
                except:
                    print(2)
                    return
    count_falls = 0
    for rr in range(rows):
        for cc in range(columns):
            if temp_falls[rr][cc]:
                count_falls += 1
                final_falls[rr][cc] = temp_falls[rr][cc]
                print("CUUUUREEEENT::", current)
                temp_board[rr][cc] = current
                # printer(temp_board)
    count = 0
    for r in range(rows):
        for c in range(columns):
            if temp_board[r][c] != EMPTY and backup_board[r][c] != EMPTY:
                if backup_falls[r][c]:
                    print('nic')
                else:
                    count += 1

    if count != 0 or (count_falls != count_new):
        print(3)
        return
    else:
        for rr in range(rows):
            for cc in range(columns):
                if falls[rr][cc]:
                    falls[rr][cc] = False
                    board[rr][cc] = EMPTY
        for r in range(rows):
            for c in range(columns):
                if temp_board[r][c] != EMPTY and backup_board[r][c] == EMPTY:
                    board[r][c] = temp_board[r][c]
                    falls[r][c] = final_falls[r][c]
    # printer(temp_falls)
    # for rr in range(rows):
    #     for cc in range(columns):
    #         if temp_falls[rr][cc]:
    #             if board[rr][cc] != EMPTY:
    #                 for r in range(rows):
    #                     for c in range(columns):
    #                         board[r][c] = backup_board[r][c]
    #                 # board = backup_board
    #                 # printer(board)
    #                 # falls = backup_falls
    #                 print("CCC")
    #                 return
    # for rr in range(rows):
    #     for cc in range(columns):
    #         if temp_falls[rr][cc]:
    #             if board[rr][cc] != EMPTY:
    #                 board = backup_board
    #                 falls = backup_falls
    #                 print("DDD")
    #                 return
    #             falls[rr][cc] = temp_falls[rr][cc]
    #             board[rr][cc] = current
    # count = 0
    # for rr in range(rows):
    #     for cc in range(columns):
    #         if temp_falls[rr][cc]:
    #             count += 1
    # if count == 0:
    #     board = backup_board
    #     falls = backup_falls
    #     print("GGG")
    #     return



# def get():
#     for rr in range(rows):
#         for cc in range(columns):
#             if falls[rr][cc]:
#                 ro = rr
#                 co = cc
#                 break
#         break

def rotate():
    paste()

def fall():
    temp_falls = [[False for _ in range(columns)] for _ in range(rows)]
    temp_board = [[EMPTY for _ in range(columns)] for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            if falls[r][c] and r + 1 < rows:
                # board[r + 1][c] = board[r][c]
                # board[r][c] = EMPTY
                # falls[r + 1][c] = True
                # falls[r][c] = False
                temp_board[r + 1][c] = board[r][c]
                board[r][c] = EMPTY
                temp_falls[r + 1][c] = falls[r][c]
                falls[r][c] = False
    for r in range(rows):
        for c in range(columns):
            if temp_falls[r][c]:
                falls[r][c] = temp_falls[r][c]
                board[r][c] = temp_board[r][c]




running = True
while running:
    clock.tick(fps)
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or event.type == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left()
            elif event.key == pygame.K_RIGHT:
                right()
            elif event.key == pygame.K_DOWN:
                fps = 10
            elif event.key == pygame.K_UP:
                rotate()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                fps = 2


    row = 0
    column = 0

    # ilosc = 0
    # for r in range(rows):
    #     for c in range(columns):
    #         if falls[r][c]:
    #             if r + 1 < rows and board[r + 1][c] != EMPTY:
    #                 if falls[r + 1][c]:
    #                     print('nic')
    #                 else:
    #                     ilosc += 1
    #             else:
    #                 print('nic')

    # if not touched:
    #     temp_falls = [[False for _ in range(columns)] for _ in range(rows)]
    #     temp_board = [[EMPTY for _ in range(columns)] for _ in range(rows)]
    #     for r in range(rows):
    #         for c in range(columns):
    #             if falls[r][c] and r + 1 < rows:
    #                 # board[r + 1][c] = board[r][c]
    #                 # board[r][c] = EMPTY
    #                 # falls[r + 1][c] = True
    #                 # falls[r][c] = False
    #                 temp_board[r + 1][c] = board[r][c]
    #                 board[r][c] = EMPTY
    #                 temp_falls[r + 1][c] = falls[r][c]
    #                 falls[r][c] = False
    #     for r in range(rows):
    #         for c in range(columns):
    #             if temp_falls[r][c]:
    #                 falls[r][c] = temp_falls[r][c]
    #                 board[r][c] = temp_board[r][c]
    #
    # else:
    #     for r in range(rows):
    #         for c in range(columns):
    #             falls[r][c] = False
    for row in range(rows):
        for column in range(columns):
            if falls[row][column] and row + 1 < rows and falls[row + 1][column] and touched is False:
                touched = False
            elif falls[row][column] and row + 1 < rows and board[row + 1][column] != EMPTY:
                # if falls[row + 1][column]:
                #     touched = False
                # else:
                touched = True
            elif falls[row][column] and row + 1 >= rows:
                touched = True
            elif board[row][column] == EMPTY and touched is False:
                touched = False

    if not touched:
        fall()
    else:
        for r in range(rows):
            for c in range(columns):
                falls[r][c] = False
    # touched = False
    while True:

        # if not touched:
        #     if row + 1 < rows and board[row + 1][column] == EMPTY:
        #         board[row + 1][column] = board[row][column]
        #         board[row][column] = EMPTY
        #         falls[row + 1][column] = True
        #         falls[row][column] = False

        # if dol(row) == 0:
        #     for c in range(columns):
        #         if falls[row][c]:
        #             board[row + 1][column] = board[row][column]
        #             board[row][column] = EMPTY
        #             falls[row + 1][column] = True
        #             falls[row][column] = False
        # else:
        #     for r in range(rows):
        #         for c in range(columns):
        #             falls[r][c] = False
        # ilosc = 0
        # for r in range(rows):
        #     for c in range(columns):
        #         if falls[r][c]:
        #             if r + 1 < rows and board[r + 1][c] != EMPTY:
        #                 if falls[r + 1][c]:
        #                     print('nic')
        #                 else:
        #                     ilosc += 1
        #             else:
        #                 print('nic')
        #
        # if ilosc == 0:
        #     temp_falls = [[False for c in range(columns)] for r in range(rows)]
        #     temp_board = [[EMPTY for c in range(columns)] for r in range(rows)]
        #     for r in range(rows):
        #         print('---')
        #         for c in range(columns):
        #             if falls[r][c]:
        #                 print(r, c)
        #                 # board[r + 1][c] = board[r][c]
        #                 # board[r][c] = EMPTY
        #                 # falls[r + 1][c] = True
        #                 # falls[r][c] = False
        #                 temp_board[r + 1][c] = board[r][c]
        #                 board[r][c] = EMPTY
        #                 temp_falls[r + 1][c] = falls[r][c]
        #                 falls[r][c] = False
        #                 for r in range(rows):
        #                     for c in range(columns):
        #                         if temp_falls[r][c]:
        #                             falls[r][c] = temp_falls[r][c]
        #                             board[r][c] = temp_board[r][c]
        # else:
        #     for r in range(rows):
        #         for c in range(columns):
        #             falls[r][c] = False
        # if row + 1 < rows and board[row + 1][column] == EMPTY:
        #     ilosc = 0
        #     for r in range(rows):
        #         for c in range(columns):
        #             if falls[r][c]:
        #                 if r + 1 < rows and board[r + 1][c] != EMPTY:
        #                     if falls[r + 1][c]:
        #                         print('nic')
        #                     else:
        #                         ilosc += 1
        #                 else:
        #                     print('nic')
        #     if ilosc == 0:
        #         board[row + 1][column] = board[row][column]
        #         board[row][column] = EMPTY
        #         falls[row + 1][column] = True
        #         falls[row][column] = False

        # if falls[row][column]:
        #     if row + 1 < rows and column - 3 >= 0 and falls[row][column - 3] is True:
        #         if board[row + 1][column - 3] == EMPTY:
        #             board[row + 1][column] = board[row][column]
        #             board[row][column] = EMPTY
        #             falls[row + 1][column] = True
        #             falls[row][column] = False
        #     elif row + 1 < rows and column + 3 < columns and falls[row][column + 3] is True:
        #         if board[row + 1][column + 3] == EMPTY:
        #             board[row + 1][column] = board[row][column]
        #             board[row][column] = EMPTY
        #             falls[row + 1][column] = True
        #             falls[row][column] = False
        #     elif row + 1 < rows and column - 2 >= 0 and falls[row][column - 2] is True:
        #         if board[row + 1][column - 2] == EMPTY:
        #             board[row + 1][column] = board[row][column]
        #             board[row][column] = EMPTY
        #             falls[row + 1][column] = True
        #             falls[row][column] = False
        #     elif row + 1 < rows and column + 2 < columns and falls[row][column + 2] is True:
        #         if board[row + 1][column + 2] == EMPTY:
        #             board[row + 1][column] = board[row][column]
        #             board[row][column] = EMPTY
        #             falls[row + 1][column] = True
        #             falls[row][column] = False
        #     elif row + 1 < rows and column + 1 < columns and falls[row][column + 1] is True:
        #         if board[row + 1][column + 1] == EMPTY:
        #             board[row + 1][column] = board[row][column]
        #             board[row][column] = EMPTY
        #             falls[row + 1][column] = True
        #             falls[row][column] = False
        #     elif row + 1 < rows and column - 1 >= 0 and falls[row][column - 1] is True:
        #         if board[row + 1][column - 1] == EMPTY:
        #             board[row + 1][column] = board[row][column]
        #             board[row][column] = EMPTY
        #             falls[row + 1][column] = True
        #             falls[row][column] = False
        #
        #     else:
        #         for r in range(rows):
        #             for c in range(columns):
        #                 falls[r][c] = False

        if check():
            set()
            spawn(board, current)
            touched = False
        if falls[1][5] is False and board[1][5] != EMPTY:
            pygame.quit()
        # ilosc = 0
        # for r in range(rows):
        #     for c in range(columns):
        #         if falls[r][c]:
        #             if r + 1 < rows and types.__contains__(board[r + 1][c]):
        #                 ilosc += 1
        #             else:
        #                 print('nic')
        # if ilosc == 0:
        #     touched = False
        # else:
        #     touched = True

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
                pygame.draw.rect(screen, color("I"),
                                 pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
                # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(column * tile_size + border_thickness, row * tile_size + border_thickness, tile_size - 2 * border_thickness, tile_size - 2 * border_thickness))
            if board[row][column] == "J":
                pygame.draw.rect(screen, color("J"),
                                 pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "L":
                pygame.draw.rect(screen, color("L"),
                                 pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "O":
                pygame.draw.rect(screen, color("O"),
                                 pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "S":
                pygame.draw.rect(screen, color("S"),
                                 pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "T":
                pygame.draw.rect(screen, color("T"),
                                 pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "Z":
                pygame.draw.rect(screen, color("Z"),
                                 pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))
            if board[row][column] == "B":
                pygame.draw.rect(screen, color("B"),
                                 pygame.Rect(column * tile_size, row * tile_size, tile_size - 3, tile_size - 3))

    pygame.draw.rect(screen, "white", pygame.Rect(columns * tile_size + 20, 20, 160, 60))
    score_text = font.render(f"Level: {level}", True, "black")
    screen.blit(score_text, (columns * tile_size + 30, 30))

    pygame.draw.rect(screen, "white", pygame.Rect(columns * tile_size + 20, 100, 160, 60))
    score_text_2 = font.render(f"Score: {points}", True, "black")
    screen.blit(score_text_2, (columns * tile_size + 30, 110))

    pygame.display.update()


def delete():
    global points, cleared_lines, level
    full_rows = []
    for r in range(rows):
        if all(board[r][c] != EMPTY for c in range(columns)):
            full_rows.append(r)

    if full_rows:
        for r in full_rows:
            del board[r]
            board.insert(0, [EMPTY for _ in range(columns)])
        cleared_lines += len(full_rows)

        if len(full_rows) == 1:
            points += single_line * level
        elif len(full_rows) == 2:
            points += double_line * level
        elif len(full_rows) == 3:
            points += triple_line * level
        elif len(full_rows) == 4:
            points += tetris_line * level

        calculate_level()


def calculate_level():
    global level, cleared_lines
    if cleared_lines == 10:
        if level < 6:
            level += 1
            cleared_lines -= 10
        else:
            level = level

    pygame.display.update()


# end
pygame.quit()
