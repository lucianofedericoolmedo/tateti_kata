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
        return self.representation[position].is_equal(token)


    def check_horizontal_win(self,token):
        win = False
        for x in range(1,4):
            win = win or self.check_horizontal_winSarasa(token,x)
        return win

    def check_horizontal_winSarasa(self,token,x):
        return self.contains_this_elem_at_position(( x , 1),token) and \
               self.contains_this_elem_at_position(( x , 2),token) and \
               self.contains_this_elem_at_position(( x , 3),token)


    def check_vertical_win(self,token):
        win = False
        for y in range(1,4):
            win = win or self.check_vertical_winSarasa(token,y)
        return win

    def check_vertical_winSarasa(self,token,y):
        return self.contains_this_elem_at_position(( 1 , y),token) and \
               self.contains_this_elem_at_position(( 2 , y),token) and \
               self.contains_this_elem_at_position(( 3 , y),token)

    def check_diagonal_win(self,token):
        return self.contains_this_elem_at_position((2, 2),token) and \
               (self.xxx(token) or self.yyy(token))

    def xxx(self,token):
        return self.contains_this_elem_at_position((1, 1),token) and \
            self.contains_this_elem_at_position((3, 3),token)

    def yyy(self,token):
        return self.contains_this_elem_at_position((1, 3),token) and \
            self.contains_this_elem_at_position((3, 1),token)

    def contains_cross_in_position(self,position):
        return self.representation[position].is_cross()

    def contains_circle_in_position(self,position):
        return self.representation[position].is_circle()

    def check_if_someone_make_diagonal_win(self):
        return self.check_diagonal_win(Cross()) or \
               self.check_diagonal_win(Circle())