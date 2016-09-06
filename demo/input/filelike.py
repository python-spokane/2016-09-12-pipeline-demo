#
# filelike.py
#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Base input processor which generates an lazy sequence of content from a file object.

See:
  https://docs.python.org/3/glossary.html#term-file-object
"""


def consume(handle):

    line = True

    while line:
        line = handle.readline()
        line = line.rstrip('\n')

        if line:
            yield line.split(' ')
