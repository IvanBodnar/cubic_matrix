from abc import ABC, abstractmethod
from enum import Enum
from typing import Tuple
from collections import namedtuple

from cubic_matrix.exceptions import CoordinateOutOfRange

# Represents a position inside the matrix.
Position = namedtuple('Position', ['x', 'y', 'z'])


class ValidActions(Enum):
    """
    Contains the valid actions, to avoid working
    with plain strings.
    """
    UPDATE = 'UPDATE'
    QUERY = 'QUERY'


class Action(ABC):
    """
    Abstract class that prescribes the interface
    that the specific actions must implement.
    """
    @staticmethod
    @abstractmethod
    def _parse_arguments(arguments: list) -> Tuple:
        pass

    @abstractmethod
    def execute(self):
        pass


class UpdateAction(Action):
    """
    Executes the logic required to implement the UPDATE action.
    Receives the matrix dict from the CubicMatrix instance.
    """
    def __init__(self, arguments: list, matrix: dict):
        self._position, self._update_value = self._parse_arguments(arguments)
        self._matrix = matrix

    @staticmethod
    def _parse_arguments(arguments: list) -> Tuple[Tuple[int], int]:
        """
        Parses the arguments passed by CubicMatrix._parse_command, separating
        the given matrix coordinate from the value to update. It's used on the
        __init__ method to create the _position and _update_value instance attributes.
        """
        return tuple(int(value)for value in arguments[0:3]), int(arguments[-1])

    def execute(self):
        """
        Assigns the given value to the matrix dictionary.
        """
        if self._position not in self._matrix:
            raise CoordinateOutOfRange('Coordinates are out of matrix range.')
        self._matrix[self._position] = self._update_value


class QueryAction(Action):
    """
    Executes the logic required to implement the QUERY action.
    Receives the matrix dict from the CubicMatrix instance.
    """
    def __init__(self, arguments: list, matrix: dict):
        self._start_position, self._end_position = self._parse_arguments(arguments)
        self._matrix = matrix

    @staticmethod
    def _parse_arguments(arguments: list) -> Tuple[Tuple[int], Tuple[int]]:
        """
        Parses the arguments passed by CubicMatrix._parse_command, separating
        both matrix coordinates. It's used on the__init__ method to create the
        _start_position and _end_position instance attributes.
        """
        int_arguments = [int(value) for value in arguments]
        start_args = tuple(int_arguments[0:3])
        end_args = tuple(int_arguments[3:])
        return start_args, end_args

    def _get_enumerated_items(self) -> Tuple:
        """
        This method is used to get the index + 1 of each matrix
        position. it returns a tuple of tuples. Each tuple has the
        index number + 1 of the element as first member, and the element
        itself as second.
        """
        return tuple(enumerate(self._matrix.items(), 1))

    def _get_index(self, position: tuple) -> int:
        """
        Uses _get_enumerated_items extract the index position of
        self._start_position and self._end_position.
        """
        enumerated_items = self._get_enumerated_items()
        return [item[0] for item in enumerated_items if item[1][0] == position][0]

    def execute(self) -> int:
        """
        Uses the tuple given by _get_enumerated_items to extract all the values of
        the matrix elements inside the range given by _start_position and _end_position,
        and returns the sum of those values.
        """
        if self._start_position not in self._matrix or self._end_position not in self._matrix:
            raise CoordinateOutOfRange('Coordinates are out of matrix range.')
        enumerated_items = self._get_enumerated_items()
        start = self._get_index(self._start_position)
        end = self._get_index(self._end_position)
        return sum(item[1][1] for item in enumerated_items if item[0] in range(start, end + 1))
