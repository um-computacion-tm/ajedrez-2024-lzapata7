from piece import Piece

class Pawn(Piece):
    def get_possible_moves(self, board, row, col):
        moves = []
        direction = -1 if self.color == 'white' else 1
        if board[row + direction][col] is None:
            moves.append((row + direction, col))
        return moves
