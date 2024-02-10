#!/usr/bin/python3
"""
defines inherted list classs MyList
"""


class MyList(list):
    """implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """prints list in sorted asc order"""
        print(sorted(self))
