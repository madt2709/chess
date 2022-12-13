import chess
from search.base import BaseSearch
from settings import MAX_PLY, MATE, INFINITE


class Minimax(BaseSearch):
    def search(self, depth, ply=0):
        """
        Search self.board with self.evaluate using the minimax algorithm. Will use the negamax variant to remove unnecessary code. 
        Params: 
        - depth: Remaining depth to search. Measured in half moves.
        - ply: depth of current node. Measured in half moves
        Returns: 
        - score: evaluation of the position
        - pv: list of variations ordered by score. The principal variation (best move) is at 0 index.
        """

        if depth <= 0:
            # nothing left to search
            return self.evaluate(), []

        if ply >= MAX_PLY:
            # stop if we exceed max ply
            return self.evaluate(), []

        if self.board.is_checkmate():
            # return the ply distnace in this case
            return -MATE + ply, []

        if self.board.is_fivefold_repetition():
            # game drawn
            return 0, []

        if self.board.is_insufficient_material():
            # game drawn
            return 0, []

        if ply > 0 and self.stop_signal():
            # stop condition triggered
            return 0, []

        best_value = -INFINITE
        pv = []
        for move in self.board.legal_moves:
            self.board.push(move)
            search_value, child_pv = self.search(depth - 1, ply + 1)
            search_value = - search_value
            self.board.pop()

            if ply > 0 and self.stop_signal():
                # check if child node has stop signal
                return 0, []

            if best_value < search_value:
                best_value, pv = search_value, [move] + child_pv

        return best_value, pv
