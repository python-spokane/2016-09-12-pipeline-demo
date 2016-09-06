#
# tcp.py
#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Input processor which generates an lazy sequence of content from a TCP socket.
"""

import socket

from demo.input import filelike


def consume(address='127.0.0.1', port=9990):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((address, port))
        sock.listen(1)

        with sock.accept() as pair:
            with open(pair[0], "r", closefd=False) as handle:
                yield from filelike.consume(handle)
