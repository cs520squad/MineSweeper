# generate a board with size = n * m, and probability
from Cell_class.py import Cell


class Board(object):
    def __init__(self, text):
        # using the asciitext to represent the board
        # blank==> zero surrounding mine with symbol '0'
        # mine with symbol '*', unknown with symbol '?', and N =[1-8] with how many mines around.
        txt = [tx_t.strip() for tx_t in text.strip().split('\n')]

        # n is the row, m is the column size relatively.
        self.n = len(txt)
        self.m = len(txt[0])

        self.cells = {}
        for row, row_id in enumerate(n):
            for column, col_id in enumerate(m):
                cell_id = (row + 1, column + 1)
                self.cells[cell_id] = Cell(col_id, self.name_cell(*cell_id))

    def adjacent_cell(self, row, column):
        for i in range(max(row-1, 1), min(row+2, self.n+1)):
            for j in range(max(column-1, 1), min(column+2, self.m+1)):
                cell_id = (i, j)
                if cell_id != (row, column):
                    yield (cell_id, self.cells[cell_id])

    def total_cell(self):
        return self.n * self.m


