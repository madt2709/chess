import chess
import random


def make_random_move(board):
    """
    Inputs: board instance
    Outputs: Makes a random legal move and returns it if possible.
    """
    # Check if there are legal moves. If there are legal moves, make a random move
    legal_moves = board.legal_moves
    if legal_moves:
        random_move = random.choice(list(legal_moves))
        board.push_san(str(random_move))
        return random_move
