#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Transformer module for the pipeline demo.
"""

from .capitalize import capitalize
from .whitespace import whitespace

__all__ = [
    'capitalize',
    'whitespace',
    'pipeline'
]


def pipeline(*coroutines):
    """
    Return a callable which iterates all passed transformers in order. Returns the
    modified content.
    """

    def wrapped(content):
        for coroutine in coroutines:
            content = coroutine(content)

        return content

    return wrapped