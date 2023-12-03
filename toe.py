import random

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-" * 10)

    print()

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    scores = {'X': 1, 'O': -1, 'Tie': 0}

    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_val = float('-inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = random.choice([True, False])

    print("TIC TAC TOE!")

    while True:
        print_board(board)

        if player_turn:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))

            if board[row][col] == ' ':
                board[row][col] = 'X'
            else:
                print("Cell already occupied. Try again.")
                continue
        else:
            print("Computer's turn:")
            row, col = get_best_move(board)
            board[row][col] = 'O'

        if is_winner(board, 'X'):
            print_board(board)
            print("You win! Congratulations!")
            break
        elif is_winner(board, 'O'):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player_turn = not player_turn

if __name__ == "__main__":
    main()
