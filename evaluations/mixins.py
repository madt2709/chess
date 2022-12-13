import chess
from evaluations.piece_valuations import PIECE_VALUATIONS
from evaluations.piece_squares import PIECE_SQUARE_TABLES


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
        for piece in chess.PIECE_TYPES:
            count = sum(1 for i in self.board.pieces(piece, chess.WHITE))
            score += count * PIECE_VALUATIONS[piece]
        for pieces in chess.PIECE_TYPES:
            count = sum(1 for i in self.board.pieces(piece, chess.BLACK))
            score -= count * PIECE_VALUATIONS[piece]

        if self.board.turn == chess.BLACK:
            score = - score

        return score + parent_score


class PieceSquareEvaluation(BaseEvaluation):
    def evaluate(self):
        parent_score = super(PieceSquareEvaluation, self).evaluate()
        score = 0
        for piece in chess.PIECE_TYPES:
            for square in self.board.pieces(piece, chess.WHITE):
                score += PIECE_SQUARE_TABLES[piece][square]
            for square in self.board.pieces(piece, chess.BLACK):
                # note you can find the horizontally mirrored square with the following formula:
                # start with x (each square is number 1,2,..,64 starting a1,a2,...,h8)
                # let y = x  mod 8
                # the mirror square = 56 + y - x if y != 0 else 64 - x
                remainder = square % 8
                if remainder != 0:
                    mirror_square = 56 + remainder - square
                else:
                    mirror_square = 64 - square
                score -= PIECE_SQUARE_TABLES[piece][mirror_square]

        if self.board.turn == chess.BLACK:
            score = -score

        return score + parent_score
