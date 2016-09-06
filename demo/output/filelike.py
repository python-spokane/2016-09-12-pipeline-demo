#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
"""


def produce(handle):

    while True:
        payload = (yield)
        payload = ' '.join(payload)
        payload = '{}\n'.format(payload)
        handle.writelines(payload)
