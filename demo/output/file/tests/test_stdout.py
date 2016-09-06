#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

import sys
from unittest import TestCase
from io import StringIO

from demo.output.file.stdout import produce


class StdoutTestCase (TestCase):

    def setUp(self):
        self.stdout = sys.stdout

    def tearDown(self):
        sys.stdout = self.stdout

    def test_simple(self):

        content = ("This", "is", "line", "1")

        # Mock out stdout with the string buffer.
        buffer = StringIO()
        sys.stdout = buffer

        coroutine = produce()
        coroutine.send(content)

        expected = ' '.join(content)
        expected = '{}\n'.format(expected)

        # The first iteration should produce the mock content.
        self.assertEqual(expected, buffer.getvalue())
