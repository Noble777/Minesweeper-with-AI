from random import randint
import pygame
import time
import player
import copy
pygame.init()



def dfs(x, y, visited, list, size):
    list.append((x, y))
    visited[x][y] = 1
    if(x < size - 1 and visited[x + 1][y] == 0):
        dfs(x + 1, y, visited, list, size)
    if(y < size - 1 and visited[x][y + 1] == 0):
        dfs(x, y + 1, visited, list, size)
    if (x > 0 and visited[x - 1][y] == 0):
        dfs(x - 1, y, visited, list, size)
    if (y > 0 and visited[x][y - 1] == 0):
        dfs(x, y - 1, visited, list, size)

# init the game
def mine(n, bombs):
    table = makeTable(n)
    table = add_bombs(table, bombs)
    table = change_table(table)
    # table = [[3, 9, 2, 0], [9, 9, 2, 0], [2, 2, 1, 0], [0, 0, 0, 0]]
    #pr(table)
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
                table = check_up_left(table, x, y)
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
        if table[x - 1][y + 1] != 9:
            table[x - 1][y + 1] += 1
    return table

def check_up(table, x, y):
    if x - 1 >= 0:
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

def pri(lst):
    length = lst.__len__()
    tt = makeTable(length)
    for i in range(length):
        for j in range(length):
            p = lst[i][j]
            if (p.visible == True):
                tt[j][i] = p.val
            else:
                tt[j][i] = -1
    return tt

def prx(lst, matrix):
    length = lst.__len__()
    tt = makeTable(length)
    for i in range(length):
        for j in range(length):
            p = lst[i][j]
            if (p.visible == True):
                tt[j][i] = p.val
            elif (p.visible == False and matrix[i][j] == 9):
                tt[j][i] = 9
                # if p.flag == False:
                #     p.flag = True
            else:
                tt[j][i] = -1
    # print "prx result"
    # for cell in tt:
    #     print cell
    return tt, lst

def prt(matrix):
    for cell in matrix:
        print cell

def changelst(lst, matrix):
    length = lst.__len__()
    # print "---------"
    # print "change result"
    # for cell in matrix:
    #     print cell
    for i in range(length):
        for j in range(length):
            p = lst[i][j]
            if (matrix[i][j] == 9):
                p.val = 9
    return lst

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
    def __len__(self):
        return len(self.numbers)

def restart(size, bombs,list):
    game(size, bombs, list)

def open_game(lst, square):
    square.visible = True
    i = square.x // 40
    j = square.y // 40
    if i + 1 < len(lst):
        # we check one cube arround the current cube if it is in the table
        # if it is and it is not visible and unflagged, open it and than, if it is
        # zero open everything arround it again and again
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
def game(size, bombs, position):
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

    #print position, '\n'
    oldlist = copy.deepcopy(position)

    run = True
    flag_run = True
    counting = 0
    pathnumber = -1
    matrix = pri(lst)
    while run:
        matrix,lst = prx(lst,matrix)
        pathnumber += 1
        #prt(matrix)
        # matrix = pri(lst)
        newPosition, position, matrix = player.playlogic(position, matrix, pathnumber)
        run = checkWin(matrix)
        #time.sleep(1)
        counting += 1
        #print counting
        #print(newPosition)
        for i in lst:
            for j in i:
                if flag_run == False:
                    break
                p = lst[newPosition[0]][newPosition[1]]
                r = pygame.rect.Rect((p.x, p.y), (1, 1))
                #print(p.val)
                if j.rect.colliderect(r):
                    if j.flag == False:
                        if j.val == 9: #there is bomb
                            # print j.val
                            return "game over"
                            run = False
                            flag_run = False
                        j.visible = True
                        if j.val == 0:
                            j.visible = open_game(lst, j)
                            j.visible = True
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
                    return "You win"
            pygame.display.update()

    # won or lost, show all bombs
    for i in lst:
        for j in i:
            if j.val == 9:
                screen.blit(nine, (j.x + 10, j.y + 10))
    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if quit the game, close the program
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run = False
                    restart(size, bombs, oldlist)  # if the user press 'r' to restart

# check whether matrix have a square which is unvisible
def checkWin(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == -1):
                return True
    return False

size = 10
bombs = 1
# search
x_axis = 0
y_axis = 0
list = []


def make_visited(n):
    return [[0] * n for i in range(n)]


visited = make_visited(size)
dfs(x_axis, y_axis, visited, list, size)
# print list, '\n'

count = 0
for i in range(100):
    oldlist = copy.deepcopy(list)
    result = game(size, bombs, oldlist)
    if (result == "You win"):
        count += 1
print count