import unittest
from board import Board
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King

class TestBoard(unittest.TestCase):

    def test_initial_board_setup(self):
        board = Board()
        self.assertIsInstance(board.board[0][0], Rook)
        self.assertIsInstance(board.board[7][7], Rook)
        self.assertIsInstance(board.board[1][0], Pawn)
        self.assertIsInstance(board.board[6][0], Pawn)

    def test_move_piece(self):
        board = Board()
        board.move_piece((1, 0), (3, 0))  # Mover peón de 1,0 a 3,0
        self.assertIsInstance(board.board[3][0], Pawn)
        self.assertIsNone(board.board[1][0])

    def test_invalid_move(self):
        board = Board()
        with self.assertRaises(IndexError):
            board.move_piece((1, 0), (8, 8))  # Movimiento inválido fuera del tablero

if __name__ == '__main__':
    unittest.main()
