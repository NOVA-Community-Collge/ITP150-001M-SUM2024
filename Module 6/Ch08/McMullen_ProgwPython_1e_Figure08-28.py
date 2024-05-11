board = [[" ", "O", "X"],
         ["O", "O", " "],
         ["X", " ", "X"]]

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end="")
        
    print()
