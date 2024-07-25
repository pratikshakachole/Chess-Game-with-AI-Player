import random

# Define the chess board
board = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]

# Define the pieces and their movements
pieces = {
    "R": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    "N": [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)],
    "B": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
    "Q": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
    "K": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
    "P": [(-1, 0), (1, 0)],  # Only for capturing, needs separate logic for forward move
    "r": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    "n": [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)],
    "b": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
    "q": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
    "k": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
    "p": [(-1, 0), (1, 0)]  # Only for capturing, needs separate logic for forward move
}

# Function to display the chess board
def display_board(board):
    print("   a b c d e f g h")
    for i in range(8):
        print(8 - i, end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print(8 - i)
    print("   a b c d e f g h")

# Function to get valid moves for a piece
def get_valid_moves(piece, row, col, board):
    valid_moves = []
    for dx, dy in pieces[piece]:
        new_row = row + dx
        new_col = col + dy
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] == ".":
                valid_moves.append((new_row, new_col))
            elif board[new_row][new_col].isupper() != piece.isupper():
                valid_moves.append((new_row, new_col))
                break
            else:
                break
    return valid_moves

# Function to get a valid move for AI player
def get_ai_move(board):
    best_move = None
    best_score = -1000
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece.islower():
                for move in get_valid_moves(piece, row, col, board):
                    # Simulate the move
                    temp_board = [row[:] for row in board]
                    temp_board[move[0]][move[1]] = temp_board[row][col]
                    temp_board[row][col] = "."

                    # Evaluate the score of the move (very simple evaluation)
                    score = evaluate_board(temp_board)
                    if score > best_score:
                        best_score = score
                        best_move = (row, col, move)
    return best_move

# Function to evaluate the board for AI (very simple evaluation)
def evaluate_board(board):
    score = 0
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece.islower():
                score += 1
            elif piece.isupper():
                score -= 1
    return score

# Function to get the user's move
def get_user_move(board):
    while True:
        move = input("Enter your move (e.g. a2 a4): ").split()
        if len(move) == 2:
            try:
                start_row = 8 - int(move[0][1])
                start_col = ord(move[0][0]) - ord('a')
                end_row = 8 - int(move[1][1])
                end_col = ord(move[1][0]) - ord('a')
                if board[start_row][start_col].isupper() and (end_row, end_col) in get_valid_moves(board[start_row][start_col], start_row, start_col, board):
                    return (start_row, start_col, (end_row, end_col))
                else:
                    print("Invalid move. Please try again.")
            except:
                print("Invalid move. Please try again.")
        else:
            print("Invalid move format. Please try again.")

# Main game loop
def play_game():
    current_player = "white"
    while True:
        display_board(board)
        if current_player == "white":
            move = get_user_move(board)
            board[move[2][0]][move[2][1]] = board[move[0]][move[1]]
            board[move[0]][move[1]] = "."
            current_player = "black"
        else:
            move = get_ai_move(board)
            if move is None:
                print("AI has no valid moves. You win!")
                break
            board[move[2][0]][move[2][1]] = board[move[0]][move[1]]
            board[move[0]][move[1]] = "."
            current_player = "white"
        # Add game ending conditions here (e.g., checkmate, stalemate)

# Start the game
play_game()