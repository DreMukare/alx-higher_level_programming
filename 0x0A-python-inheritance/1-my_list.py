#!/usr/bin/python3
""" 1-my_list: MyList """


class MyList(list):
    """
        class MyList
        inherits from list
        Methods:
            print_sorted: prints sorted list
    """
    def print_sorted(self):
        """
            prints list sorted in ascending order
        """
        print(sorted(self))
