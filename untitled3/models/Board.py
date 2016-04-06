from models.Token import Cross, Circle
from .CustomExceptions import PositionAlreadyTakenException


class Board(object):
    def __init__(self):
        self.representation = {}

    def add_element(self,element,position):
        if self.contains_element_at_position(position):
            raise PositionAlreadyTakenException
        self.representation[position] = element

    def contains_element_at_position(self,position):
        return self.representation.has_key(position)

    #lambda x : x.funcion()
    def contains_this_elem_at_position(self,position,token):
        if self.contains_element_at_position(position):
            return self.representation[position].is_equal(token)


    def check_horizontal_win(self,token):
        win = False
        for row in range(1,4):
            win = win or self.check_horizontal_winSarasa(token,row)
        return win

    def check_horizontal_winSarasa(self,token,row):
        return self.contains_this_elem_at_position(( row , 1),token) and \
               self.contains_this_elem_at_position(( row , 2),token) and \
               self.contains_this_elem_at_position(( row , 3),token)


    def check_vertical_win(self,token):
        win = False
        for column in range(1,4):
            win = win or self.check_vertical_winSarasa(token,column)
        return win

    def check_vertical_winSarasa(self, token, column):
        return self.contains_this_elem_at_position((1 , column), token) and \
               self.contains_this_elem_at_position((2 , column), token) and \
               self.contains_this_elem_at_position((3 , column), token)

    def check_diagonal_win(self,token):
        return self.contains_this_elem_at_position((2, 2),token) and \
               (self.contains_upper_and_lower_horizontal(token) or self.contains_upper_and_lower_diagonal(token))

    def contains_upper_and_lower_horizontal(self, token):
        return self.contains_this_elem_at_position((1, 1),token) and \
            self.contains_this_elem_at_position((3, 3),token)

    def contains_upper_and_lower_diagonal(self, token):
        print
        return self.contains_this_elem_at_position((1, 3),token) and \
            self.contains_this_elem_at_position((3, 1),token)

    def contains_cross_in_position(self,position):
        return self.representation[position].is_cross()

    def contains_circle_in_position(self,position):
        return self.representation[position].is_circle()

    def check_if_someone_make_diagonal_win(self):
        return self.check_diagonal_win(Cross()) or \
               self.check_diagonal_win(Circle())