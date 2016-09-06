#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
"""

from string import capwords
from demo import coroutine


def capitalize():

    coroutine = generator()

    def wrapped(content):
        return coroutine.send(content)

    return wrapped


@coroutine
def generator():

    payload = None

    while True:
        payload = (yield payload)
        payload = [capwords(w) for w in payload]
