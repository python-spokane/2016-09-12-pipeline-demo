#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Filter used to detect if content is too large to process.
"""

from demo import coroutine


def size(max_length=8):
    """
    Filter performing size checks on streaming content. If the content is larger
    than max_length, this filter will return None.

    Returns a callable function which wraps the internal filtering coroutine, and
    drives iteration via generator send().
    """

    coroutine = generator(max_length)

    def wrapped(content):
        return coroutine.send(content)

    return wrapped


@coroutine
def generator(max_length):
    """
    Internal generator which maintains previously seen messages, along with their count.
    """

    payload = None

    while True:
        payload = (yield payload)

        if len(payload) > max_length:
            payload = None
