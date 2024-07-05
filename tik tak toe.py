import math

# Constants
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Function to print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a winner or a draw
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != EMPTY:
            return board[combo[0]]
    if EMPTY not in board:
        return 'DRAW'
    return None

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner == 'DRAW':
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Function to determine the AI's move
def ai_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    board[move] = AI

# Function to determine the human's move
def human_move(board, move):
    if board[move] == EMPTY:
        board[move] = HUMAN
        return True
    return False

# Main game loop
def play_game():
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Human's turn
        human_move_made = False
        while not human_move_made:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move < 9:
                    human_move_made = human_move(board, move)
                    if not human_move_made:
                        print("Invalid move! Try again.")
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Enter a number between 1 and 9.")

        print_board(board)
        if check_winner(board):
            break

        # AI's turn
        print("AI is making a move...")
        ai_move(board)
        print_board(board)
        if check_winner(board):
            break

    winner = check_winner(board)
    if winner == 'DRAW':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

# Start the game
if __name__ == "_main_":
    play_game()