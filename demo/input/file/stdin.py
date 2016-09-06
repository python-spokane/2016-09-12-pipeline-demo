#
# stdin.py
#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Input processor which generates an lazy sequence of content from STDIN.
"""

import sys

from demo.input import filelike


def consume(**_):

    yield from filelike.consume(sys.stdin)
