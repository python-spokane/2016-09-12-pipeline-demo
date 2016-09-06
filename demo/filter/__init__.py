#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Filter module for the pipeline demo.
"""

from demo.filter.size import size
from demo.filter.duplicate import duplicate

__all__ = [
    'size',
    'duplicate',
    'pipeline'
]


def pipeline(*coroutines):
    """
    Return a callable which iterates all passed filters in order. Returns the
    original content if successful, None if filtered.
    """

    def wrapped(content):
        for coroutine in coroutines:
            content = coroutine(content)

            if not content:
               return None

        return content

    return wrapped