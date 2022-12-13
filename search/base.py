import chess


class BaseSearch():
    def __init__(self, board: chess.Board):
        if board is None:
            raise ValueError("board must be defined")
        self.board = board

    def stop_signal(self):
        return False
