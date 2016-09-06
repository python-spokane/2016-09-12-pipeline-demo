#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
"""

import sys

from demo import coroutine
from demo.output import filelike


def produce():

    coroutine = generator()

    def wrapped(content):
        return coroutine.send(content)

    return wrapped


@coroutine
def generator():

    yield from filelike.produce(sys.stdout)
