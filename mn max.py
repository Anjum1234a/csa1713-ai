import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for player in ['X', 'O']:
        # Rows, columns and diagonals
        for row in board:
            if all(cell == player for cell in row):
                return player
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return player
        if all(board[i][i] == player for i in range(3)):
            return player
        if all(board[i][2 - i] == player for i in range(3)):
            return player
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"

    while True:
        print_board(board)
        if check_winner(board) or is_full(board):
            break

        # Human move
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Invalid input. Enter numbers.")
                continue
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = human
                break
            else:
                print("Invalid move, try again.")

        if check_winner(board) or is_full(board):
            break

        # AI move
        i, j = best_move(board)
        board[i][j] = ai
        print(f"AI plays: ({i}, {j})")

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
