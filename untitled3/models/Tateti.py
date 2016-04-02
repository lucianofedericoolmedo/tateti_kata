from CustomExceptions import PlayerMovedTwiceInARowException
from models.Board import Board
from models.Token import Cross, Circle,Token


class Tateti(object):
    def __init__(self):
        self.board = Board()
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

