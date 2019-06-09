from cubic_matrix.exceptions import NonIntegerArgument, InvalidAction


def integers_validation(arguments: list):
    """
    Checks that all given arguments are ints.
    Raises an exception otherwise.
    """
    for arg in arguments:
        try:
            int(arg)
        except ValueError:
            raise NonIntegerArgument('Argument "{}" is not valid, must be an integer.'.format(arg))


def action_validation(action: str):
    """
    Checks that the given action is a valid action.
    Raises an exception otherwise.
    """
    if action.strip().upper() not in ('QUERY', 'UPDATE'):
        raise InvalidAction('Action "{}" is not valid. Options are UPDATE and QUERY.'.format(action))
