from typing import Dict

from cubic_matrix.exceptions import InvalidAction
from cubic_matrix.actions import ValidActions, UpdateAction, QueryAction, Position


class CubicMatrix:
    def __init__(self, columns: int, rows: int, depth: int):
        self._matrix = {
            Position(x, y, z): 0
            for z in range(1, depth + 1)
            for x in range(1, columns + 1)
            for y in range(1, rows + 1)
        }

    @property
    def matrix(self) -> Dict[Position, int]:
        return self._matrix

    def _parse_command(self, command: str):
        action, *args = command.split()
        if action.strip() == ValidActions.UPDATE.name:
            return UpdateAction(args, self._matrix)
        elif action == ValidActions.QUERY.name:
            return QueryAction(args, self._matrix)
        else:
            raise InvalidAction('Action {} is not valid. Options are UPDATE and QUERY'.format(action))
