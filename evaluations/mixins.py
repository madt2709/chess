import chess
from evaluations.piece_valuations import PIECE_VALUATIONS


class BaseEvaluation():
    def __init__(self, board):
        if board is None:
            raise ValueError("board must be defined")
        self.board = board

    def evaluate(self):
        return 0


class PieceEvaluation(BaseEvaluation):
    def evaluate(self):
        parent_score = super(PieceEvaluation, self).evaluate()
        score = 0
        for pieces in chess.PIECE_TYPES:
            count = sum(1 for i in self.board.pieces(pieces, chess.WHITE))
            score += count * PIECE_VALUATIONS[pieces]
        for pieces in chess.PIECE_TYPES:
            count = sum(1 for i in self.board.pieces(pieces, chess.BLACK))
            score -= count * PIECE_VALUATIONS[pieces]

        if self.board.turn == chess.BLACK:
            score = - score

        return score + parent_score
