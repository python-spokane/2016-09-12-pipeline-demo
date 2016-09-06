#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Transformer used to remove whitespace from all strings in the content.
"""

from re import compile, sub
from demo import coroutine


def whitespace():
    """
    Transformer returning a modified list of content after whitespace removal.

    Returns a callable function which wraps the internal transforming coroutine, and
    drives iteration via generator send().
    """

    coroutine = generator()

    def wrapped(content):
        return coroutine.send(content)

    return wrapped


@coroutine
def generator():
    """
    Internal generator performs content whitespace removal.
    """

    compiled = compile(r'(^\s+|\s+$)')
    payload = None

    while True:
        payload = (yield payload)
        payload = [sub(compiled, '', w) for w in payload]
