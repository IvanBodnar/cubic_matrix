from collections import namedtuple
from enum import Enum
from typing import Dict

from .exceptions import InvalidAction


Position = namedtuple('Position', ['x', 'y', 'z'])
UpdateAction = namedtuple('UpdateAction', ['position', 'value'])
QueryAction = namedtuple('QueryAction', ['positions'])


class Actions(Enum):
    UPDATE = 'UPDATE'
    QUERY = 'QUERY'


class CubicMatrix:
    def __init__(self, rows: int, columns: int, depth: int):
        self._matrix = {
            Position(x, y, z): 0
            for z in range(1, depth + 1)
            for y in range(1, columns + 1)
            for x in range(1, rows + 1)
        }

    @property
    def matrix(self) -> Dict[Position, int]:
        return self._matrix

    @staticmethod
    def _parse_command(command: str):
        action, *args = command.split()
        if action == Actions.UPDATE:
            return UpdateAction(tuple(args[0:3]), args[-1])
        elif action == Actions.QUERY:
            return QueryAction(args)
        else:
            raise InvalidAction('Action {} is not valid. Options are UPDATE and QUERY'.format(action))
