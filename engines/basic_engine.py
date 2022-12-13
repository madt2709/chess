import chess
from evaluations.mixins import PieceEvaluation
from search.minimax import Minimax
from settings import DEPTH


class BasicEngine(PieceEvaluation, Minimax):
    def make_move(self):
        score, pv = self.search(DEPTH)
        print(chess.COLOR_NAMES[self.board.turn],
              score, " ".join(map(str, pv)))
        self.board.push(pv[0])
