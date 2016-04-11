from .Token import Cross, Circle, EmptyToken
from .CustomExceptions import PositionAlreadyTakenException
from .Lines import row, Line, column, slash_diagonal, backSlash_diagonal
from _functools import reduce


class Board(object):
    
    ##############     Init     ##############
    def __init__(self, rows, columns):
        self.representation = self._init_map(rows, columns)
        self.rows = self._init_rows(rows, columns)
        self.columns = self._init_columns(rows, columns)
        self.diagonals = self._init_diagonals()
    
    def _init_map(self, rows, columns):
        cell = {}
        for r in range(rows):
            for c in range(columns):
                cell[row(r)[c]] = EmptyToken()
        return cell
    
    def _init_rows(self, rows, columns):
        res = []
        for r in range(rows):
            local_row = Line(self.representation)
            for c in range(columns):
                local_row.positions[c] = row(r)[c]
            res.append(local_row)
        return res
    
    def _init_columns(self, rows, columns):
        res = []
        for c in range(columns):
            local_column = Line(self.representation)
            for r in range(rows):
                local_column.positions[r] = column(c)[r]
            res.append(local_column)
        return res
    
    def _init_diagonals(self):
        res = [Line(self.representation), Line(self.representation)]
        for i in range(3):
            res[0].positions[i] = slash_diagonal()[i]
        for i in range(3):
            res[1].positions[i] = backSlash_diagonal()[i]
        return res
    
    
    ##############     Public interface     ##############
    
    def add_element(self,element,position):
        if self.contains_element_at_position(position):
            raise PositionAlreadyTakenException
        self.representation[position] = element

    def contains_element_at_position(self,position):
        return not self.representation[position].is_empty()

    def contains_this_elem_at_position(self,position,token):
        if self.contains_element_at_position(position):
            return self.representation[position].is_equal(token)

    def check_horizontal_win(self, token):
        return reduce(lambda x, y: x or y, map(lambda local_row: local_row.line_full_with(token), self.rows))

    def check_vertical_win(self,token):
        return reduce(lambda x,y: x or y, map(lambda col: col.line_full_with(token), self.columns))

    def check_diagonal_win(self,token):
        return reduce(lambda x,y: x or y, map(lambda diag: diag.line_full_with(token), self.diagonals))

    def contains_cross_in_position(self,position):
        return self.representation[position].is_cross()

    def contains_circle_in_position(self,position):
        return self.representation[position].is_circle()

    def check_if_someone_make_diagonal_win(self):
        return self.check_diagonal_win(Cross()) or \
               self.check_diagonal_win(Circle())