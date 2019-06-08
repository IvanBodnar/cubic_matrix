from enum import Enum
from typing import Tuple
from collections import namedtuple


Position = namedtuple('Position', ['x', 'y', 'z'])


class ValidActions(Enum):
    UPDATE = 'UPDATE'
    QUERY = 'QUERY'


class UpdateAction:
    def __init__(self, arguments: list, matrix: dict):
        self._position, self._update_value = self._parse_arguments(arguments)
        self._matrix = matrix

    @staticmethod
    def _parse_arguments(arguments: list) -> Tuple[Tuple[int], int]:
        return tuple(int(value)for value in arguments[0:3]), int(arguments[-1])

    def execute(self):
        self._matrix[self._position] = self._update_value
        print(self._matrix)
