
def success_message(result: str or int):
    print('SUCCESS {}'.format(result if result is not None else ''))


def error_message(detail: str):
    print('ERROR {}'.format(detail or ''))
