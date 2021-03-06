#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

from io import StringIO
from unittest import TestCase

from demo.input.filelike import consume


def as_buffer(content):

    return StringIO(content)


def combine(content):

    return '\n'.join(content)


def expected_format(content):
    return [c.split(' ') for c in content]


class FilelikeTestCase (TestCase):

    def test_single_line(self):

        content = ("This is line 1", )
        buffer = as_buffer(combine(content))
        expected = expected_format(content)

        # Manual iteration..
        generator = consume(buffer)

        # The first iteration should produce the mock content.
        self.assertEqual(expected.pop(), next(generator))

        # EOF should raise a StopIteration..
        with self.assertRaises(StopIteration):
            next(generator)

    def test_multiple_lines(self):

        content = ("This is line 1", "This is line 2", "This is line 3")
        buffer = as_buffer(combine(content))
        expected = expected_format(content)

        # Manual iteration..
        generator = consume(buffer)

        # Each iteration chunk was produced from the mock content.
        for index, _ in enumerate(content):
            self.assertEqual(expected.pop(0), next(generator))

        # Then StopIteration..
        with self.assertRaises(StopIteration):
            next(generator)

    def test_multiple_lines_embedded_eof(self):
        content = ("This is line 1", "This is line 2", '', "This is line 4")
        buffer = as_buffer(combine(content))
        expected = expected_format(content)

        # Manual iteration..
        generator = consume(buffer)

        # Each iteration chunk was produced from the mock content.
        for index, _ in enumerate((content[0], content[1])):
            self.assertEqual(expected.pop(0), next(generator))

        # Then StopIteration on line 3.
        with self.assertRaises(StopIteration):
            next(generator)

        # Never reach line 4.
