# tic_tac_toe_ai.py

import math

# Initialize board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(brd, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(brd[i] == player for i in combo) for combo in win_combos)

def is_draw(brd):
    return ' ' not in brd

def get_available_moves(brd):
    return [i for i, spot in enumerate(brd) if spot == ' ']

def minimax(brd, is_maximizing):
    if is_winner(brd, 'O'):
        return {'score': 1}
    elif is_winner(brd, 'X'):
        return {'score': -1}
    elif is_draw(brd):
        return {'score': 0}

    if is_maximizing:
        best = {'score': -math.inf}
        for move in get_available_moves(brd):
            brd[move] = 'O'
            sim_score = minimax(brd, False)
            brd[move] = ' '
            sim_score['move'] = move
            if sim_score['score'] > best['score']:
                best = sim_score
        return best
    else:
        best = {'score': math.inf}
        for move in get_available_moves(brd):
            brd[move] = 'X'
            sim_score = minimax(brd, True)
            brd[move] = ' '
            sim_score['move'] = move
            if sim_score['score'] < best['score']:
                best = sim_score
        return best

def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X', AI is 'O'")
    print_board()

    while True:
        # Human turn
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'
        print_board()

        if is_winner(board, 'X'):
            print(" You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # AI turn
        print("AI is thinking...")
        ai_move = minimax(board, True)['move']
        board[ai_move] = 'O'
        print_board()

        if is_winner(board, 'O'):
            print(" AI wins! Better luck next time.")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Run the game
play_game()

