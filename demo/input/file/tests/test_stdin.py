#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

import sys
from unittest import TestCase
from io import StringIO

from demo.input.file.stdin import consume


def as_buffer(content):

    return StringIO(content)


def combine(content):

    return '\n'.join(content)


class StdinTestCase (TestCase):

    def setUp(self):
        self.stdin = sys.stdin

    def tearDown(self):
        sys.stdin = self.stdin

    def test_single_line(self):

        content = ("This is line 1", )
        buffer = as_buffer(combine(content))

        # Mock out stdin with the string buffer.
        sys.stdin = buffer

        # Manual iteration..
        generator = consume()

        # The first iteration should produce the mock content.
        self.assertEqual(content[0], next(generator))

        # EOF should raise a StopIteration..
        with self.assertRaises(StopIteration):
            next(generator)

    def test_multiple_lines(self):

        content = ("This is line 1", "This is line 2", "This is line 3")
        buffer = as_buffer(combine(content))

        # Mock out stdin with the string buffer.
        sys.stdin = buffer

        # Manual iteration..
        generator = consume()

        # Each iteration chunk was produced from the mock content.
        for index, _ in enumerate(content):
            self.assertEqual(content[index], next(generator))

        # Then StopIteration..
        with self.assertRaises(StopIteration):
            next(generator)

    def test_multiple_lines_embedded_eof(self):
        content = ("This is line 1", "This is line 2", '', "This is line 4")
        buffer = as_buffer(combine(content))

        # Mock out stdin with the string buffer.
        sys.stdin = buffer

        # Manual iteration..
        generator = consume()

        # Each iteration chunk was produced from the mock content.
        for index, _ in enumerate((content[0], content[1])):
            self.assertEqual(content[index], next(generator))

        # Then StopIteration on line 3.
        with self.assertRaises(StopIteration):
            next(generator)

        # Never reach line 4.
