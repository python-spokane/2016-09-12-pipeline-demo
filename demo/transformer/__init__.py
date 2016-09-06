#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
"""

from .capitalize import capitalize
from .whitespace import whitespace

__all__ = [
    'capitalize',
    'whitespace',
    'pipeline'
]


def pipeline(*coroutines):

    def wrapped(content):

        for coroutine in coroutines:
            content = coroutine(content)

        return content

    return wrapped