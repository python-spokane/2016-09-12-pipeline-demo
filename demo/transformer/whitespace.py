#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
"""

from re import compile, sub
from demo import coroutine


def whitespace():

    coroutine = generator()

    def wrapped(content):
        return coroutine.send(content)

    return wrapped


@coroutine
def generator():

    compiled = compile(r'(^\s+|\s+$)')
    payload = None

    while True:
        payload = (yield payload)
        payload = [sub(compiled, '', w) for w in payload]
