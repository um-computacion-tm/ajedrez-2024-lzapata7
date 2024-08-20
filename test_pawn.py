import unittest
from board import Board
from pawn import Pawn

class TestPawn(unittest.TestCase):

    def test_pawn_move(self):
        board = Board()
        moves = board.board[1][0].get_possible_moves(board.board, 1, 0)
        self.assertIn((2, 0), moves)

    def test_pawn_blocked_move(self):
        board = Board()
        board.board[2][0] = Pawn('white')
        moves = board.board[1][0].get_possible_moves(board.board, 1, 0)
        self.assertNotIn((2, 0), moves)

if __name__ == '__main__':
    unittest.main()
