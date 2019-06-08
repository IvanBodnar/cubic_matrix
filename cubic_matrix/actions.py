from abc import ABC, abstractmethod
from enum import Enum
from typing import Tuple
from collections import namedtuple


Position = namedtuple('Position', ['x', 'y', 'z'])


class ValidActions(Enum):
    UPDATE = 'UPDATE'
    QUERY = 'QUERY'


class Action(ABC):
    @staticmethod
    @abstractmethod
    def _parse_arguments(arguments: list) -> Tuple:
        pass

    @abstractmethod
    def execute(self):
        pass


class UpdateAction(Action):
    def __init__(self, arguments: list, matrix: dict):
        self._position, self._update_value = self._parse_arguments(arguments)
        self._matrix = matrix

    @staticmethod
    def _parse_arguments(arguments: list) -> Tuple[Tuple[int], int]:
        return tuple(int(value)for value in arguments[0:3]), int(arguments[-1])

    def execute(self):
        self._matrix[self._position] = self._update_value


class QueryAction(Action):
    def __init__(self, arguments: list, matrix: dict):
        self._start_position, self._end_position = self._parse_arguments(arguments)
        self._matrix = matrix

    @staticmethod
    def _parse_arguments(arguments: list) -> Tuple[Tuple[int], Tuple[int]]:
        int_arguments = [int(value) for value in arguments]
        start_args = tuple(int_arguments[0:3])
        end_args = tuple(int_arguments[3:])
        return start_args, end_args

    def _get_enumerated_items(self) -> Tuple:
        return tuple(enumerate(self._matrix.items(), 1))

    def _get_index(self, position: tuple) -> int:
        enumerated_items = self._get_enumerated_items()
        return [item[0] for item in enumerated_items if item[1][0] == position][0]

    def execute(self):
        enumerated_items = self._get_enumerated_items()
        start = self._get_index(self._start_position)
        end = self._get_index(self._end_position)
        return sum(item[1][1] for item in enumerated_items if item[0] in range(start, end + 1))
