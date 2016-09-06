#
# stdin.py
#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Input generator which consumes an lazy sequence of content from STDIN.
"""

import sys

from demo.input import filelike


def consume(**_):
    """
    Lazily read STDIN as a file-like object.
    """

    # Delegate to the file-like object consumer.
    yield from filelike.consume(sys.stdin)
