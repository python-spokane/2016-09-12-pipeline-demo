#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Filter used to detect if content has been seen previously.
"""

from demo import coroutine

__all__ = ['duplicate']


def duplicate():
    """
    Filter performing de-duplication on streaming content. If the content has been
    previously been seen, this filter will return None.

    Returns a callable function which wraps the internal filtering coroutine, and
    drives iteration via generator send().
    """

    coroutine = generator()

    def wrapped(content):
        return coroutine.send(content)

    return wrapped


@coroutine
def generator():
    """
    Internal generator which maintains previously seen messages, along with their count.
    """

    payload, seen = None, {}

    while True:
        payload = (yield payload)

        # Lists aren't hashable, so join to a string for internal state.
        key = ' '.join(payload)

        if key in seen:
            seen[key] += 1
            payload = None
        else:
            seen[key] = 1
