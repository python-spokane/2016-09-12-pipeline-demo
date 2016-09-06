#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

from io import StringIO
from unittest import TestCase
from unittest.mock import patch, mock_open

from demo.input.network.tcp import consume


def as_buffer(content):

    return StringIO(content)


def combine(content):

    return '\n'.join(content)


class TcpTestCase (TestCase):

    @patch('demo.input.network.tcp.socket')
    def test_single_line(self, _):

        content = ("This is line 1", )

        with patch('demo.input.network.tcp.open', mock_open(read_data=combine(content))):
            # Manual iteration..
            generator = consume()

            # The first iteration should produce the mock content.
            self.assertEqual(content[0], next(generator))

            # EOF should raise a StopIteration..
            with self.assertRaises(StopIteration):
                next(generator)

    @patch('demo.input.network.tcp.socket')
    def test_multiple_lines(self, _):

        content = ("This is line 1", "This is line 2", "This is line 3")

        with patch('demo.input.network.tcp.open', mock_open(read_data=combine(content))):
            # Manual iteration..
            generator = consume()

            # Each iteration chunk was produced from the mock content.
            for index, _ in enumerate(content):
                self.assertEqual(content[index], next(generator))

            # Then StopIteration..
            with self.assertRaises(StopIteration):
                next(generator)

    @patch('demo.input.network.tcp.socket')
    def test_multiple_lines_embedded_eof(self, _):

        content = ("This is line 1", "This is line 2", '', "This is line 4")

        with patch('demo.input.network.tcp.open', mock_open(read_data=combine(content))):
            # Manual iteration..
            generator = consume()

            # Each iteration chunk was produced from the mock content.
            for index, _ in enumerate((content[0], content[1])):
                self.assertEqual(content[index], next(generator))

            # Then StopIteration on line 3.
            with self.assertRaises(StopIteration):
                next(generator)

            # Never reach line 4.
