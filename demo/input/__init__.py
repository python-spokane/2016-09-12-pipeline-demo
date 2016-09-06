#
# Written by Franco Gasperino <franco.gasperino@gmail.com>, 2016
#

"""
Input module for the pipeline demo.
"""

from demo.input.file.stdin import consume as stdin
from demo.input.network.tcp import consume as tcp

__all__ = [
    'stdin',
    'tcp'
]
