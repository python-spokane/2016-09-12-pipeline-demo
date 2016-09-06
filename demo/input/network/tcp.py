#
# tcp.py
#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Input generator which consumes an lazy sequence of content from a TCP socket.
"""

import socket

from demo.input import filelike


def consume(address='127.0.0.1', port=9990):
    """
    Lazily read a TCP/IP client as a file-like object.

    Consumption is stopped once the client is no longer present.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((address, port))
        sock.listen(1)

        # Wrap the socket in a file-like object, and delegate consumption.
        with sock.accept() as pair:
            with open(pair[0], "r", closefd=False) as handle:
                yield from filelike.consume(handle)
