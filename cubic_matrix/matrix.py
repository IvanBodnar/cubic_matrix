from collections import namedtuple
from typing import Dict


Position = namedtuple('Position', ['x', 'y', 'z'])


class CubicMatrix:
    def __init__(self, rows: int, columns: int, depth: int):
        self._matrix = {
            Position(x, y, z): 0
            for z in range(1, depth + 1)
            for y in range(1, columns + 1)
            for x in range(1, rows + 1)
        }

    @property
    def matrix(self) -> Dict[Position]:
        return self._matrix
