def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def minimax(board, depth, is_maximizing):
    scores = {
        "X": -1,
        "O": 1,
        "draw": 0
    }

    if check_winner(board, "X"):
        return scores["X"]
    if check_winner(board, "O"):
        return scores["O"]
    if is_board_full(board):
        return scores["draw"]

    if is_maximizing:
        max_eval = float("-inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            evaluation = minimax(board, depth + 1, False)
            board[row][col] = " "
            max_eval = max(max_eval, evaluation)
        return max_eval
    else:
        min_eval = float("inf")
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            evaluation = minimax(board, depth + 1, True)
            board[row][col] = " "
            min_eval = min(min_eval, evaluation)
        return min_eval

def computer_move(board):
    best_move = None
    best_score = float("-inf")

    for row, col in get_empty_cells(board):
        board[row][col] = "O"
        score = minimax(board, 0, False)
        board[row][col] = " "

        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move

def tic_tac_toe():
    current_player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        if current_player == "X":
            row = int(input("Player X, choose row (0, 1, 2): "))
            col = int(input("Player X, choose column (0, 1, 2): "))
        else:
            row, col = computer_move(board)
            print(f"Computer O chooses row {row} and column {col}")

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                if current_player == "X":
                    print("Player X wins!")
                else:
                    print("Computer O wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
