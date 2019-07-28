from My_Array import Array


class Grid(object):
    """Response a two-dimensional array."""

    def __init__(self, rows, columns, fill_value=None):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fill_value)

    def get_height(self):
        """Returns the number of rows."""
        return len(self._data)

    def get_width(self):
        """Return the number of columns."""
        return len(self._data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [row][column]"""
        return self._data[index]

    def __str__(self):
        """Return a string representation of the grid."""
        result = ''
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self._data[row][col]) + ' '
            result += '\n'
        return result
