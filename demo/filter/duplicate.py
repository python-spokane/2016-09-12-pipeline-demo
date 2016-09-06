#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
"""

from demo import coroutine

__all__ = ['duplicate']


def duplicate():

    coroutine = generator()

    def wrapped(content):
        return coroutine.send(content)

    return wrapped


@coroutine
def generator():

    payload, seen = None, {}

    while True:
        payload = (yield payload)

        key = ' '.join(payload)

        if key in seen:
            seen[key] += 1
            payload = None
        else:
            seen[key] = 1

