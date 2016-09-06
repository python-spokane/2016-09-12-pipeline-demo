#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

from unittest import TestCase

from demo.filter.size import size


class SizeTest (TestCase):

    def test_pass(self):

        content = ['This', 'is', 'the', 'payload']

        coroutine = size(100)
        response = coroutine(content)

        self.assertEqual(content, response)

    def test_filtered(self):
        content = ['This', 'is', 'the', 'payload']

        coroutine = size(max_length=2)
        response = coroutine(content)

        self.assertIsNone(response)
