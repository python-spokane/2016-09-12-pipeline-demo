#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

from unittest import TestCase

from demo.transformer.capitalize import capitalize


class CapitalizeTest (TestCase):

    expected = ['This', 'Is', 'The', 'Payload']

    def test_no_change(self):

        content = ('This', 'Is', 'The', 'Payload')

        coroutine = capitalize()
        response = coroutine(content)

        self.assertEqual(CapitalizeTest.expected, response)

    def test_one(self):

        content = ('This', 'Is', 'the', 'Payload')

        coroutine = capitalize()
        response = coroutine(content)

        self.assertEqual(CapitalizeTest.expected, response)

    def test_several(self):
        content = ('this', 'Is', 'the', 'payload')

        coroutine = capitalize()
        response = coroutine(content)

        self.assertEqual(CapitalizeTest.expected, response)
