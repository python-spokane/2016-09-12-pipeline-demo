#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
"""

from demo import input as inputs
from demo import output as outputs
from demo import filter as filters
from demo import transformer as transformers


def stdin_stdout():

    source = inputs.stdin()
    sink = outputs.stdout()

    for payload in source:
        sink(payload)


def stdin_size_stdout():

    source = inputs.stdin()
    sink = outputs.stdout()

    pipeline = filters.pipeline(
        filters.size(max_length=12)
    )

    for payload in source:
        payload = pipeline(payload)

        if not payload:
            continue

        sink(payload)


def stdin_size_duplicate_stdout():

    source = inputs.stdin()
    sink = outputs.stdout()

    pipeline = filters.pipeline(
        filters.size(max_length=12),
        filters.duplicate()
    )

    for payload in source:
        payload = pipeline(payload)

        if not payload:
            continue

        sink(payload)


def stdin_capitalize_stdout():

    source = inputs.stdin()
    sink = outputs.stdout()

    pipeline = transformers.pipeline(
        transformers.capitalize()
    )

    for payload in source:
        payload = pipeline(payload)
        sink(payload)


if __name__ == '__main__':
    stdin_stdout()
