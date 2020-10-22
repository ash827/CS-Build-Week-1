from board import Board

def main():
    # created so a user can input rows and columns
    user_rows = int(input('How many rows would you like? '))
    user_columns = int(input('How about columns? '))

    # create a board:
    game_of_life_board = Board(user_rows,user_columns)

    # run the first iteration of the board:
    game_of_life_board.draw_board()
    # game_of_life_board.update_board()

    # need generations
    user_action = ''
    while user_action != 'q':
        user_action = input('Press "Enter" to add a generation or "q" to quit:')

        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()


main()