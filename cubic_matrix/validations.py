from cubic_matrix.exceptions import NonIntegerArgument, InvalidAction


def integers_validation(arguments: list):
    for arg in arguments:
        try:
            int(arg)
        except ValueError:
            raise NonIntegerArgument('Argument "{}" is not valid, must be an integer.'.format(arg))


def action_validation(action: str):
    if action.strip().upper() not in ('QUERY', 'UPDATE'):
        raise InvalidAction('Action {} is not valid. Options are UPDATE and QUERY'.format(action))
