#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Sample pipeline assembly for the demo.
"""

from demo import input as inputs
from demo import output as outputs
from demo import filter as filters
from demo import transformer as transformers


def stdin_stdout():
    """
    Consumes input from the STDIN source, and produces output on the STDOUT sink.

    Filters:
      None
    Transformers:
      None
    """

    source = inputs.stdin()
    sink = outputs.stdout()

    for payload in source:
        sink(payload)


def stdin_size_stdout():
    """
    Consumes input from the STDIN source, applies filtering, and produces output on the STDOUT sink.

    Filtering:
      size - limited to 12 words

    Transformers:
      None
    """

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
    """
    Consumes input from the STDIN source, applies filtering, and produces output on the STDOUT sink.

    Filtering:
      size - limited to 12 words
      duplicate - no repeated lines

    Transformers:
      None
    """

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
    """
    Consumes input from the STDIN source, applies transformations, and produces output on the STDOUT sink.

    Filtering:
        None

    Transformers:
      capitalization - each word will be capitalized
    """

    source = inputs.stdin()
    sink = outputs.stdout()

    pipeline = transformers.pipeline(
        transformers.capitalize()
    )

    for payload in source:
        payload = pipeline(payload)
        sink(payload)


def stdin_size_duplicate_capitalize_whitespace_stdout():

    source = inputs.stdin()
    sink = outputs.stdout()

    filter_pipeline = filters.pipeline(
        filters.size(max_length=12),
        filters.duplicate()
    )

    transform_pipeline = transformers.pipeline(
        transformers.capitalize(),
        transformers.whitespace()
    )

    for payload in source:
        payload = filter_pipeline(payload)

        if payload:
            payload = transform_pipeline(payload)
            sink(payload)


if __name__ == '__main__':
    stdin_stdout()
