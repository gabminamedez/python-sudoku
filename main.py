import pygame
import time
from solver import isPossible, solve

def drawBoard(surface):
    global errors
    global playTime

    surface.fill((255, 255, 255))

    pygame.draw.line(surface, (0, 0, 0), (0, 0), (540, 0), 5)
    pygame.draw.line(surface, (0, 0, 0), (0, 60), (540, 60), 1)
    pygame.draw.line(surface, (0, 0, 0), (0, 120), (540, 120), 1)
    pygame.draw.line(surface, (0, 0, 0), (0, 180), (540, 180), 5)
    pygame.draw.line(surface, (0, 0, 0), (0, 240), (540, 240), 1)
    pygame.draw.line(surface, (0, 0, 0), (0, 300), (540, 300), 1)
    pygame.draw.line(surface, (0, 0, 0), (0, 360), (540, 360), 5)
    pygame.draw.line(surface, (0, 0, 0), (0, 420), (540, 420), 1)
    pygame.draw.line(surface, (0, 0, 0), (0, 480), (540, 480), 1)
    pygame.draw.line(surface, (0, 0, 0), (0, 540), (540, 540), 5)

    pygame.draw.line(surface, (0, 0, 0), (0, 0), (0, 540), 5)
    pygame.draw.line(surface, (0, 0, 0), (60, 0), (60, 540), 1)
    pygame.draw.line(surface, (0, 0, 0), (120, 0), (120, 540), 1)
    pygame.draw.line(surface, (0, 0, 0), (180, 0), (180, 540), 5)
    pygame.draw.line(surface, (0, 0, 0), (240, 0), (240, 540), 1)
    pygame.draw.line(surface, (0, 0, 0), (300, 0), (300, 540), 1)
    pygame.draw.line(surface, (0, 0, 0), (360, 0), (360, 540), 5)
    pygame.draw.line(surface, (0, 0, 0), (420, 0), (420, 540), 1)
    pygame.draw.line(surface, (0, 0, 0), (480, 0), (480, 540), 1)
    pygame.draw.line(surface, (0, 0, 0), (540, 0), (540, 540), 5)

    font = pygame.font.SysFont("comicsans", 40)

    err = font.render('Errors: ' + str(errors), True, (255, 0, 0))
    surface.blit(err, (10, 560))

    time = font.render(formatTime(playTime), True, (0,128,0))
    surface.blit(time, (560 - 110, 560))

def formatTime(secs):
    sec = secs % 60
    minute = secs // 60
    hour = minute // 60

    if sec < 10:
        final = " " + str(minute) + " : 0" + str(sec)
    else:
        final = " " + str(minute) + " : " + str(sec)

    return final

def drawNums(surface, grid):
    font = pygame.font.SysFont("comicsans", 70)

    w = 18
    h = 10

    for row in range(9):
        if row == 3 or row == 6:
            h += 5
        if row == 8:
            h += 5

        for col in range(9):
            if col == 3 or col == 6:
                w += 5
            if col == 8:
                w += 5

            if grid[row][col] == 0:
                num = font.render('', True, (0, 0, 0))
            else:
                num = font.render(str(grid[row][col]), True, (0, 0, 0))
            surface.blit(num, (w, h))

            w += 58

        w = 18
        h += 58

def drawClick(surface, pos):
    global curRow
    global curCol

    if pos[0] < 540 and pos[1] < 540:
        if pos[0] > 0 and pos[0] < 60:
            curCol = 0
        elif pos[0] > 60 and pos[0] < 120:
            curCol = 1
        elif pos[0] > 120 and pos[0] < 180:
            curCol = 2
        elif pos[0] > 180 and pos[0] < 240:
            curCol = 3
        elif pos[0] > 240 and pos[0] < 300:
            curCol = 4
        elif pos[0] > 300 and pos[0] < 360:
            curCol = 5
        elif pos[0] > 360 and pos[0] < 420:
            curCol = 6
        elif pos[0] > 420 and pos[0] < 480:
            curCol = 7
        elif pos[0] > 480 and pos[0] < 540:
            curCol = 8

        if pos[1] > 0 and pos[1] < 60:
            curRow = 0
        elif pos[1] > 60 and pos[1] < 120:
            curRow = 1
        elif pos[1] > 120 and pos[1] < 180:
            curRow = 2
        elif pos[1] > 180 and pos[1] < 240:
            curRow = 3
        elif pos[1] > 240 and pos[1] < 300:
            curRow = 4
        elif pos[1] > 300 and pos[1] < 360:
            curRow = 5
        elif pos[1] > 360 and pos[1] < 420:
            curRow = 6
        elif pos[1] > 420 and pos[1] < 480:
            curRow = 7
        elif pos[1] > 480 and pos[1] < 540:
            curRow = 8

        rowDiv = (pos[0] // 60) * 60
        colDiv = (pos[1] // 60) * 60

        pygame.draw.line(surface, (0, 128, 0), (rowDiv, colDiv), (rowDiv + 60, colDiv), 5)
        pygame.draw.line(surface, (0, 128, 0), (rowDiv, colDiv + 60), (rowDiv + 60, colDiv + 60), 5)
        pygame.draw.line(surface, (0, 128, 0), (rowDiv, colDiv), (rowDiv, colDiv + 60), 5)
        pygame.draw.line(surface, (0, 128, 0), (rowDiv + 60, colDiv), (rowDiv + 60, colDiv + 60), 5)

def insNum(num):
    global board
    global curRow
    global curCol
    global errors

    if board[curRow][curCol] == 0:
        if isPossible(board, (curRow, curCol), num):
            board[curRow][curCol] = num
        else:
            errors += 1

pygame.init()

screen = pygame.display.set_mode((540, 600))
pygame.display.set_caption('Sudoku')

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

clickPos = (10, 10)
curRow = -1
curCol = -1
key = None
errors = 0
timeStart = time.time()

running = True
while running:
    playTime = round(time.time() - timeStart)

    drawBoard(screen)
    drawNums(screen, board)
    drawClick(screen, clickPos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            drawClick(screen, clickPos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = 1
            if event.key == pygame.K_2:
                key = 2
            if event.key == pygame.K_3:
                key = 3
            if event.key == pygame.K_4:
                key = 4
            if event.key == pygame.K_5:
                key = 5
            if event.key == pygame.K_6:
                key = 6
            if event.key == pygame.K_7:
                key = 7
            if event.key == pygame.K_8:
                key = 8
            if event.key == pygame.K_9:
                key = 9

            insNum(key)

    pygame.display.update()