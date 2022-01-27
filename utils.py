# LIBRARIES

# We need to draw a board.

board = [" "] * 10

def draw_board(board):
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("---+---+---")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])

# We need to know which symbol the 1st player wants to play as

def assign_symbols():
    symbol = 'wrong'

    while symbol not in ["X", "O"]:
        symbol = input("Player 1: Do you want to play as 'X' or 'O'? ").upper()


    if symbol == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def player_move(current_player):
    move = 'wrong'

    while move not in range(1,10):
        try:
            move = int(input(f"{current_player}: Pick a board's position (1-9): "))
        except ValueError:
            print("Oops! Invalid input. Make sure to enter only numbers from 1 to 9")
    
    return move

def check_winner(indices):
    pass


def check_win(b, dict_players, current_player):
    combinations = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3))
    for condition in combinations:
        if (b[condition[0]] == b[condition[1]] == b[condition[2]] == dict_players[current_player]):
            return True
    return False

# dry code

def check_for_yes_or_no(question):
    yes_or_no = ''

    while yes_or_no not in ['Y', 'N', 'YES', 'NO']:
        yes_or_no = input(question + ' [y/n]: ').upper()

        if yes_or_no not in ['Y', 'N', 'YES', 'NO']:
            print('Sorry! Wrong answer. You must enter yes or no')

    # returns Y or N
    return yes_or_no[0]