import chess
from engines import random_move_generator

"""
A function to run the engine.
"""


def play_against_engine():
    # create board
    board = chess.Board()

    # ask user for which side they want to play on
    user_response = ""
    while user_response not in ['W', 'B']:
        user_response = input(
            "Would you like to play as white or black? W/B \n")
    if user_response == 'W':
        user_side = chess.WHITE
    else:
        user_side = chess.BLACK

    # play game
    while not board.is_game_over():
        print(f"{board} /n")

        if board.turn == user_side:
            user_move = input(
                "Where would you like to move? Please write moves in form e2e4, g1f3, etc.. \n")
            while user_move not in [str(i) for i in board.legal_moves]:
                user_move = input(
                    f"{user_move} is not a legal move. Please enter a legal move \n")

            board.push_san(user_move)
        else:
            random_move_generator.make_random_move(board)

    # Print the final position and game over reason
    print(board)
    if board.is_checkmate():
        print('Checkmate!')
    elif board.is_insufficient_material():
        print('Draw by insufficient material!')
    elif board.is_stalemate():
        print('Draw by stalemate!')
    elif board.is_seventyfive_moves():
        print('Draw by 75-move rule!')
    elif board.is_fivefold_repetition():
        print('Draw by 5-fold repetition!')
    else:
        print('Unexpected game over!?')
