#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
"""

__all__ = [
    'coroutine'
]


def coroutine(func):

    def wrapped(*args, **kwargs):
        coro = func(*args, **kwargs)
        next(coro)
        return coro

    return wrapped
