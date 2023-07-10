#!/usr/bin/python3
"""
module prints list
"""


class MyList(list):
    """
    class module that inherits from list
    """

    def print_sorted(self):
        '''
        prints the list in an ascending sort
        '''
        print(sorted(self))
