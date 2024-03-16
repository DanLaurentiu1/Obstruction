from texttable import Texttable


class Board:
    def __init__(self, width, height):
        self._collum = width
        self._row = height
        self.data = [[' '] * self._collum for _ in range(self._row)]
        # self.data is the a list of lists that "makes" the table
        # the first list in data will be the first row, the last list in data will be the last row

    def __str__(self):
        """
        used the first time the table is printed out, because the table is all empty
        :return: the table
        """
        table = Texttable()
        table.set_cols_align(['c'] * self._collum)
        for _ in range(self._row):
            table.add_row([' '] * self._row)
        return table.draw()
