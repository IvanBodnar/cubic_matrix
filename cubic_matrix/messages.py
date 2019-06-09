
"""
Functions to format the messages required by the business.
"""


def success_message(result: str or int):
    return 'SUCCESS {}'.format(str(result) if result is not None else '').strip()


def error_message(detail: str):
    return 'ERROR {}'.format(detail or '')
