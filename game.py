# LIBRARIES
import utils
import random

# Initial board
board = [" "] * 10
instr = ["#","1","2","3","4","5","6","7","8","9"]

def game_on():
    
    while True:
        # Define player's symbol ("X" or "O")
        markers = utils.assign_symbols() 

        #Randomize the first player
        dict_players = {
            'Player 1': markers[0], # X
            'Player 2': markers[1]  # O
            }

        initial_player = random.choice(list(dict_players.keys()))

        print(f"{initial_player} will go first playing as '{dict_players[initial_player]}'")

        current_player = initial_player
        board_status = []
        
        while True:

            #draw the board 
            utils.draw_board(board) 

            # Ask their input and place it on the board.
            position = utils.player_move(current_player)

            board[position] = dict_players[current_player]
            board_status.append(dict_players[current_player])
            print(board_status)

            #Check if the game is won, tied, lost, or ongoing
            winner = utils.check_win(board, dict_players, current_player)

            if winner: 
                utils.draw_board(board)
                print(f"{current_player} wins!")
                break
            if len(board_status) == 9:
                print("It's a tie!")
                break

            # Toggle between players 
            if current_player == "Player 1":
                current_player = "Player 2"
            else:
                current_player = "Player 1"

        yes_or_no = utils.check_for_yes_or_no("Do you want to play again?")

        if yes_or_no == 'Y':
            continue
        else:
            print("Bye-bye!")
            break
        
# GAME
print("Welcome to Tic Tac Toe!")
print("Instructions:")
utils.draw_board(instr)

yes_or_no = utils.check_for_yes_or_no("Are you ready to play?")

if yes_or_no == 'N':
    print('Bye-bye!')
else:
    game_on()

