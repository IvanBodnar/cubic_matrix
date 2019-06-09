from typing import Dict

from cubic_matrix.exceptions import InvalidAction, NonIntegerArgument, CoordinateOutOfRange
from cubic_matrix.actions import ValidActions, Action, UpdateAction, QueryAction, Position
from cubic_matrix.validations import integers_validation, action_validation
from cubic_matrix.messages import success_message, error_message


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

    def _parse_command(self, command: str) -> Action:
        action, *args = command.split()
        action_validation(action)
        integers_validation(args)
        if action.upper() == ValidActions.UPDATE.name:
            return UpdateAction(args, self._matrix)
        elif action.upper() == ValidActions.QUERY.name:
            return QueryAction(args, self._matrix)

    def execute(self, command: str):
        try:
            action = self._parse_command(command)
            result = action.execute()
            success_message(result)
        except NonIntegerArgument as e:
            error_message(str(e))
        except InvalidAction as e:
            error_message(str(e))
        except CoordinateOutOfRange as e:
            error_message(str(e))
