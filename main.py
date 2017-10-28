import minesweeper


print("Starting game")
print("press 'r' for restart")
size = int(input("Please enter the size of matrix: "))
bombs = int(input("Please enter the number of bombs: "))

# search
x_axis = 0
y_axis = 0
list = []


def make_visited(n):
    return [[0] * n for i in range(n)]


visited = make_visited(size)
minesweeper.dfs(x_axis, y_axis, visited, list, size)
# print list, '\n'
minesweeper.game(size, bombs, list)
