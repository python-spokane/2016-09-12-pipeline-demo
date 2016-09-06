#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
"""

from itertools import chain

from demo.filter.size import size
from demo.filter.duplicate import duplicate

__all__ = [
    'size',
    'duplicate',
    'pipeline'
]


def pipeline(*coroutines):

    def wrapped(content):

        for coroutine in coroutines:
            content = coroutine(content)

            if not content:
               return None

        return content

    return wrapped