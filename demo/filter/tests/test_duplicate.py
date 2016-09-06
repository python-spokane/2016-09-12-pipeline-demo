#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

from unittest import TestCase

from demo.filter.duplicate import duplicate


class DuplicateTest (TestCase):

    def test_pass(self):

        content = ['This', 'is', 'the', 'payload']

        coroutine = duplicate()
        response = coroutine(content)

        self.assertEqual(content, response)

    def test_filtered(self):

        content = (
            ('This', 'is', 'the', 'payload'),
            ('This', 'is', 'the', 'payload'),
            ('This', 'is', 'the', 'payload'),
            ('But', 'this', 'is', 'different')
        )

        coroutine = duplicate()

        replies = list(filter(lambda x: x is not None, (coroutine(c) for c in content)))
        self.assertEqual(2, len(replies))
