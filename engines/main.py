import chess

"""
A function to run the engine.
"""


def main(engine):
    # create board
    board = chess.Board()

    # ask user for which side they want to play on
    user_response = []
    while user_response not in ['W', 'B']:
        user_response = input("Would you like to play as white or black? W/B")
    if user_response == 'W':
        user_side = chess.WHITE
    else:
        user_side = chess.BLACK

    while not board.is_game_over():
        print(board)

        if board.turn == user_side:
            user_move = input(
                "Where would you like to move? Please write moves in form e2e4, g1f3, etc..")
