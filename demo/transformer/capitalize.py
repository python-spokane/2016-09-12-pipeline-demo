#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Transformer used to capitalize all strings in the content.
"""

from string import capwords
from demo import coroutine


def capitalize():
    """
    Transformer returning a modified list of content which after capitalization.

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
    Internal generator performs content capitalization.
    """

    payload = None

    while True:
        payload = (yield payload)
        payload = [capwords(w) for w in payload]
