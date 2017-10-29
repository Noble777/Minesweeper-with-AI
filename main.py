import minesweeper

print("Starting game")
print("If you want to restart the game, press 'r' ")
# size = int(input("Please enter the size of matrix: "))
# bombs = int(input("Please enter the number of bombs: "))
size = 8
bombs = 4
# search
x_axis = 0
y_axis = 0
list = []


def make_visited(n):
    return [[0] * n for i in range(n)]


visited = make_visited(size)
minesweeper.dfs(x_axis, y_axis, visited, list, size)
# print list, '\n'

result = minesweeper.game(size, bombs, list)
# print result