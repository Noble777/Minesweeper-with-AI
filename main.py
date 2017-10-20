import minesweeper


print("Starting game")
print("press 'r' for restart")
size = int(input("Please enter the size of matrix: "))
bombs = int(input("Please enter the number of bombs: "))
position = dfs()
minesweeper.game(size, bombs, position)
