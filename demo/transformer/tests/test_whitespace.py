#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

from unittest import TestCase

from demo.transformer.whitespace import whitespace


class WhitespaceTest (TestCase):

    expected = ['This', 'is', 'the', 'payload']

    def test_skip(self):

        content = ('This', 'is', 'the', 'payload')

        coroutine = whitespace()
        response = coroutine.send(content)

        self.assertEqual(WhitespaceTest.expected, response)

    def test_skip_leading(self):
        content = ('  This', 'is', 'the', 'payload')

        coroutine = whitespace()
        response = coroutine.send(content)

        self.assertEqual(WhitespaceTest.expected, response)

    def test_skip_trailing(self):
        content = ('  This', 'is', 'the', 'payload ')

        coroutine = whitespace()
        response = coroutine.send(content)

        self.assertEqual(WhitespaceTest.expected, response)

    def test_skip_leading_and_trailing(self):
        content = ('  This', 'is', 'the', 'payload ')

        coroutine = whitespace()
        response = coroutine.send(content)

        self.assertEqual(WhitespaceTest.expected, response)
