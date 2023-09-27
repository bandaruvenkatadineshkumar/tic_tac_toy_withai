import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # Check for a draw
    if all([cell != ' ' for row in board for cell in row]):
        return 'draw'

    return None

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells

def minimax(board, depth, maximizing_player):
    if check_winner(board) == 'X':
        return -1
    if check_winner(board) == 'O':
        return 1
    if check_winner(board) == 'draw':
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_empty_cells(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth+1, False)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_empty_cells(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth+1, True)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    max_eval = float('-inf')
    best_move = None
    for move in get_empty_cells(board):
        board[move[0]][move[1]] = 'O'
        eval = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move

# Main game loop
board = [[' ' for _ in range(3)] for _ in range(3)]

while True:
    print_board(board)
    user_row = int(input("Enter row (0, 1, or 2): "))
    user_col = int(input("Enter column (0, 1, or 2): "))

    if board[user_row][user_col] == ' ':
        board[user_row][user_col] = 'X'
        if check_winner(board) == 'X':
            print_board(board)
            print("You win!")
            break
        elif check_winner(board) == 'draw':
            print_board(board)
            print("It's a draw!")
            break
        else:
            ai_move = best_move(board)
            board[ai_move[0]][ai_move[1]] = 'O'
            if check_winner(board) == 'O':
                print_board(board)
                print("AI wins!")
                break
            elif check_winner(board) == 'draw':
                print_board(board)
                print("It's a draw!")
                break
    else:
        print("Invalid move. Try again.")