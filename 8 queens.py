def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, 8)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row == 8:
        print_board(board)
        return True

    res = False
    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1) or res
            board[row][col] = 0  # Backtrack
    return res

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

# Initialize the board
board = [[0 for _ in range(8)] for _ in range(8)]

# Solve the problem
solve_n_queens(board, 0)
