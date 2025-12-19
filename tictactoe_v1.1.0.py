import random

# Create the board
board = [" " for _ in range(9)]

# Winning combinations
win = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columns
    [0, 4, 8], [2, 4, 6]               # diagonals
]

def print_board():
    """Show the board in 3x3 format"""
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(symbol):
    """Check if a player with symbol X or O has won"""
    for combo in win:
        if all(board[i] == symbol for i in combo):
            return True
    return False

def available_moves():
    """Return list of empty positions"""
    return [i for i in range(9) if board[i] == " "]

# --- Difficulty Levels ---
def computer_easy():
    return random.choice(available_moves())

def computer_medium():
    # Try to win
    for combo in win:
        values = [board[i] for i in combo]
        if values.count("O") == 2 and values.count(" ") == 1:
            return combo[values.index(" ")]
    # Try to block player
    for combo in win:
        values = [board[i] for i in combo]
        if values.count("X") == 2 and values.count(" ") == 1:
            return combo[values.index(" ")]
    # Else random
    return computer_easy()

def computer_hard():
    # Simple minimax for beginners
    best_score = -999
    best_move = None
    for move in available_moves():
        board[move] = "O"
        score = minimax(False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if not available_moves():
        return 0

    if is_maximizing:
        best = -999
        for move in available_moves():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best = max(best, score)
        return best
    else:
        best = 999
        for move in available_moves():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best = min(best, score)
        return best

# --- Game Modes ---
def single_player(difficulty):
    print_board()
    while True:
        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue
        if move not in range(9) or board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"
        print_board()
        if check_winner("X"):
            print("Player wins!")
            break
        if not available_moves():
            print("It's a draw!")
            break

        # Computer move
        if difficulty == "easy":
            comp = computer_easy()
        elif difficulty == "medium":
            comp = computer_medium()
        else:
            comp = computer_hard()

        board[comp] = "O"
        print("Computer chose:", comp+1)
        print_board()
        if check_winner("O"):
            print("Computer wins!")
            break
        if not available_moves():
            print("It's a draw!")
            break

def two_player():
    print_board()
    turn = 0
    while True:
        try:
            move = int(input(f"Player {turn%2+1} enter move (1-9): ")) - 1
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue
        if move not in range(9) or board[move] != " ":
            print("Invalid move. Try again.")
            continue
        symbol = "X" if turn % 2 == 0 else "O"
        board[move] = symbol
        print_board()
        if check_winner(symbol):
            print(f"Player {turn%2+1} wins!")
            break
        if not available_moves():
            print("It's a draw!")
            break
        turn += 1

# --- Main Menu ---
mode = input("Choose mode: (1) Single Player (2) Two Player: ")
if mode == "1":
    diff = input("Choose difficulty: easy / medium / hard: ").lower()
    single_player(diff)
else:
    two_player()