from random import randint
import pygame
import time
pygame.init()


# init the game
def mine(n, bombs):
    table = makeTable(n)
    table = add_bombs(table, bombs)
    table = change_table(table)
    return table

# make a table matrix
def makeTable(n):
    return [[0] * n for i in range(n)]

# add bombs to the matrix
def add_bombs(table, bombs):
    for i in range(bombs):
        is_bomb = False
        while not is_bomb:
            x = randint(0, len(table) - 1)
            y = randint(0, len(table) - 1)
            # 9 means that there is a bomb
            if table[x][y] != 9:
                table[x][y] = 9
                is_bomb = True
    return table

# change the numbers around the bombs
def change_table(table):
    for x in range(len(table)):
        for y in range(len(table[x])):
            if table[x][y] == 9:
                table = check_down_left(table, x, y)
                table = check_down_right(table, x, y)
                table = check_down(table, x, y)
                table = check_up_left(table, x ,y)
                table = check_up_right(table, x, y)
                table = check_up(table, x, y)
                table = check_left(table, x, y)
                table = check_right(table, x, y)
    return table

def check_down_left(table, x, y):
    # check if the left-down is in the corner
    if x + 1 < len(table[x]) and y - 1 >= 0:
        # change is there is not a bomb
        if table[x + 1][y - 1] != 9:
            table[x + 1][y - 1] += 1
    return table

def check_down_right(table, x, y):
    # check if the right-down is in the corner
    if x + 1 < len(table[0]) and y + 1 < len(table):
        if table[x + 1][y + 1] != 9:
            table[x + 1][y + 1] += 1
    return table

def check_down(table, x, y):
    # check if the down is in the corner
    if x + 1 < len(table[0]):
        if table[x + 1][y] != 9:
            table[x + 1][y] += 1
    return table

def check_up_left(table, x, y):
    if x - 1 >= 0 and y - 1 >= 0:
        if table[x - 1][y - 1] != 9:
            table[x - 1][y - 1] += 1
    return table

def check_up_right(table, x, y):
    if x - 1 >= 0 and y + 1 < len(table):
        if table[x -1][y + 1] != 9:
            table[x - 1][y + 1] += 1
    return table

def check_up(table, x, y):
    if y - 1 >= 0:
        if table[x - 1][y] != 9:
            table[x - 1][y] += 1
    return table

def check_left(table, x, y):
    if y - 1 >= 0:
        if table[x][y - 1] != 9:
            table[x][y - 1] += 1
    return table

def check_right(table, x, y):
    if y + 1 < len(table):
        if table[x][y + 1] != 9:
            table[x][y + 1] += 1
    return table

def pr(table):
    for i in table:
        print(i)

#the whole board
class Board:
    def __init__(self, board):
        self.board = board
    def __repr__(self):
        pr(self.board)
        return "is your table"

# every square in the board
class Square:
    def __init__(self, x, y, w, h, board, ij):
        self.rect = pygame.rect.Rect(x, y, w, h)
        i, j = ij
        self.val = board[i][j]
        self.x = x
        self.y = y
        self.visible = False
        self.flag = False

def restart(size, bombs):
    game(size, bombs)

def open_game(lst, square):
    square.visible = True
    i = square.x // 40
    j = square.y // 40
    if i + 1 < len(lst):
        # we check one cube around the current cube if it is in the table
        # if it is and it is not visible and unflagged, open it and than, if it is
        # zero open everything around it again and again
        if lst[i + 1][j].visible == False and lst[i + 1][j].flag == False:
            lst[i + 1][j].visible = True
            if lst[i + 1][j].val == 0:
                open_game(lst, lst[i + 1][j])
        if j + 1 < len(lst):
            if lst[i + 1][j + 1].visible == False and lst[i + 1][j + 1].flag == False:
                lst[i + 1][j + 1].visible = True
                if lst[i + 1][j + 1].val == 0:
                    open_game(lst, lst[i + 1][j + 1])
        if j - 1 >= 0:
            if lst[i + 1][j - 1].visible == False and lst[i + 1][j - 1].flag == False:
                lst[i + 1][j - 1].visible = True
                if lst[i + 1][j - 1].val == 0:
                    open_game(lst, lst[i + 1][j - 1])
    if i - 1 >= 0:
        if lst[i - 1][j].visible == False and lst[i - 1][j].flag == False:
            lst[i - 1][j].visible = True
            if lst[i - 1][j].val == 0:
                open_game(lst, lst[i - 1][j])
        if j + 1 < len(lst):
            if lst[i - 1][j + 1].visible == False and lst[i - 1][j + 1].flag == False:
                lst[i - 1][j + 1].visible = True
                if lst[i - 1][j + 1].val == 0:
                    open_game(lst, lst[i - 1][j + 1])
        if j - 1 >= 0:
            if lst[i - 1][j - 1].visible == False and lst[i - 1][j - 1].flag == False:
                lst[i - 1][j - 1].visible = True
                if lst[i - 1][j - 1].val == 0:
                    open_game(lst, lst[i - 1][j - 1])
    if j - 1 >= 0:
        if lst[i][j - 1].visible == False and lst[i][j -1].flag == False:
            lst[i][j - 1].visible = True
            if lst[i][j - 1].val == 0:
                open_game(lst, lst[i][j - 1])
    if j + 1 < len(lst):
        if lst[i][j + 1].visible == False and lst[i][j + 1].flag == False:
            lst[i][j + 1].visible = True
            if lst[i][j + 1].val == 0:
                open_game(lst, lst[i][j + 1])

#position from dfs
def game(size, bombs,position):
    clicked = pygame.image.load("tile_clicked.png")
    unclicked = pygame.image.load("tile_plain.png")

    zero = pygame.image.load("tile_0.png")
    one = pygame.image.load("tile_1.png")
    two = pygame.image.load("tile_2.png")
    three = pygame.image.load("tile_3.png")
    four = pygame.image.load("tile_4.png")
    five = pygame.image.load("tile_5.png")
    six = pygame.image.load("tile_6.png")
    seven = pygame.image.load("tile_7.png")
    eight = pygame.image.load("tile_8.png")
    nine = pygame.image.load("tile_mine.png") #bomb
    flag = pygame.image.load("tile_flag.png")

    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

    MyBoard = Board(mine(size, bombs))
    w = h = len(MyBoard.board) * 40

    screen = pygame.display.set_mode((w, h))

    # create a list of all squares
    lst = [[] for i in range(size)]
    for i in range(0, size*40, 40):
        for j in range(0, size*40, 40):
            lst[i//40] += [Square(i, j, 40, 40, MyBoard.board, (i // 40, j // 40))]
            screen.blit(unclicked, (i, j))



    for newPosition in position:
         # use position to uncover block
        for i in lst:
            for j in i:
                r = pygame.rect.Rect(newPosition, (1, 1))
                if j.rect.colliderect(r):
                    if j.flag == False:
                        if j.val == 9: #there is bomb
                            print("game over")
                        j.visible = True
                        if j.val == 0:
                            j.visible = open_game(lst, j)
                            j.visible = True
            time.sleep(3)


        # open every square that visible and check win
        for i in lst:
            for j in i:
                if j.visible == True:
                    screen.blit(unclicked, (j.x, j.y))
                    screen.blit(numbers[j.val], (j.x + 10, j.y + 10))
                if j.flag == True:
                    screen.blit(flag, (j.x + 10, j.y + 10))
                if j.flag == False and j.visible == False:
                    screen.blit(clicked, (j.x, j.y))

        count = 0
        for i in lst:
            for j in i:
                if j.visible == True and j.val != 9:
                  count += 1
                # count the visible square, if open all but not a bomb, win
            if count == size * size - bombs:
                run = False
                print("You win")
        pygame.display.update()

    # won or lost, show all bombs
    for i in lst:
        for j in i:
            if j.val == 9:
                screen.blit(nine, (j.x + 10, j.y + 10))
    pygame.display.update()

    # wait for quit or rest
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if quit the game, close the program
                run = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run = False
                    restart(size, bombs)  # if the user press 'r' to restart
