def check_winner(board):
    k = len(board)
    symbols = ["X", "O"]

    for i in range(k):
        for symbol in symbols:
            if all(cell == symbol for cell in board[i]) or all(board[j][i] == symbol for j in range(k)):
                return symbol

    for symbol in symbols:
        if all(board[i][i] == symbol for i in range(k)) or all(board[i][k-i-1] == symbol for i in range(k)):
            return symbol

    return "Ничья"

board = [["X", "O", "_"],
         ["X", "X", "O"],
         ["O", "X", "O"]]

winner = check_winner(board)
print(winner)
