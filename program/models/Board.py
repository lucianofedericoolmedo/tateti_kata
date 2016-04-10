from .Token import Cross, Circle, Token
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
        map = {}
        for r in [int for _ in range(rows)]:
            for c in [int for _ in range(columns)]:
                map.insert(row(r)[c], Token())
        return map
    
    def _init_rows(self, rows, columns):
        res = []
        for r in [int for _ in range(rows)]:
            localRow = Line([])
            for c in [int for _ in range(columns)]:
                localRow.positions[c] = self.representation[row(r)[c]]
            res.append(localRow)
        return res
    
    def _init_columns(self, rows, columns):
        res = []
        for c in [int for _ in range(columns)]:
            localColumn = Line([])
            for r in [int for _ in range(rows)]:
                localColumn.positions[r] = self.representation[column(c)[r]]
            res.append(localColumn)
        return res
    
    def _init_diagonals(self):
        res = [Line([]), Line([])]
        for i in [int for _ in range(3)]:
            res[0].positions[i] = self.representation[slash_diagonal(i)]
        for i in [int for _ in range(3)]:
            res[1].positions[i] = self.representation[backSlash_diagonal(i)]
        return res
    
    
    ##############     Public interface     ##############
    
    def add_element(self,element,position):
        if self.contains_element_at_position(position):
            raise PositionAlreadyTakenException
        self.representation[position] = element

    def contains_element_at_position(self,position):
        return self.representation.has_key(position)

    def contains_this_elem_at_position(self,position,token):
        if self.contains_element_at_position(position):
            return self.representation[position].is_equal(token)


    def check_horizontal_win(self,token):
        return reduce(lambda x,y: x or y, map(lambda row: row.line_full_with(token), self.rows))

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