board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

print("\n".join(["|".join(row) for row in board]))

rowX = int(input("Player X row: "))
colX = int(input("Player X column: "))

board[rowX][colX] = "X"

print("\n".join(["|".join(row) for row in board]))

rowO = int(input("Player O row: "))
colO = int(input("Player O column: "))

board[rowO][colO] = "O"

print("\n".join(["|".join(row) for row in board]))