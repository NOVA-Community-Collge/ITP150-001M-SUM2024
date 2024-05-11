board = [[" ", " ", " "],
         ["O", "O", "X"],
         ["X", "X", "O"]]

print("\n".join(["|".join(row) for row in board]))

if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
    print("There is a winning combination on the top row!")
else:
    print("No winning combinations yet!")
