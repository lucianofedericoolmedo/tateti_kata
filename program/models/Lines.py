from _functools import reduce
from .Token import EmptyToken


def backSlash_diagonal():
    return [(0,0), (1,1), (2,2)]


def slash_diagonal():
    return [(0,2), (1,1), (2,0)]


def row(r):
    return [(r,0), (r,1), (r,2)]


def column(c):
    return [(0,c), (1,c), (2,c)]


class Line:
    
    def __init__(self, representation):
        self.positions = [(int, int) for _ in range(3)]
        self.representation = representation

    def line_full_with(self, token):
        return reduce(lambda x, y: x and y, map(lambda p: self.representation[p].is_equal(token), self.positions))
