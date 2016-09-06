#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

from demo import coroutine


def size(max_length=8):

    coroutine = generator(max_length)

    def wrapped(content):
        return coroutine.send(content)

    return wrapped


@coroutine
def generator(max_length):

    payload = None

    while True:
        payload = (yield payload)

        if len(payload) > max_length:
            payload = None
