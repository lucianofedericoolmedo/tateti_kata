from .Board import Board
from .Token import Cross, Circle,Token
from .CustomExceptions import PlayerMovedTwiceInARowException


class Tateti(object):
    def __init__(self):
        self.board = Board(3,3)
        self.last_move = Token()

    def put_cross(self,position):
        self.make_move(Cross(),position)

    def put_circle(self,position):
        self.make_move(Circle(),position)

    def make_move(self, token, position):
        if self.last_move.is_equal(token):
            raise PlayerMovedTwiceInARowException
        self.last_move = token
        self.board.add_element(token, position)

    def cross_make_diagonal_winner(self):
        return self.board.check_diagonal_win(Cross())

    def circle_make_diagonal_winner(self):
        return self.board.check_diagonal_win(Circle())

    def cross_make_horizontal_win(self):
        return self.board.check_horizontal_win(Cross())


    def circle_make_horizontal_win(self):
        return self.board.check_horizontal_win(Circle())

    def cross_make_vertical_win(self):
        return self.board.check_vertical_win(Cross())


    def circle_make_vertical_win(self):
        return self.board.check_vertical_win(Circle())

    def someone_win(self):
        return (self.circle_make_diagonal_winner() or
            self.cross_make_diagonal_winner() or
            self.circle_make_horizontal_win() or
            self.cross_make_horizontal_win() or
            self.circle_make_vertical_win() or
            self.cross_make_vertical_win())