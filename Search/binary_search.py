from typing import List

""" Assume that the array is already sorted and then halve the list """


def binart_search(iterable: List, index: int):

    middle = len(iterable) // 2

    if iterable[middle] == index:
        return middle
    elif iterable[middle] > index:
        return "item is in the other half"


def test_linear_search():

    print(binart_search([0, 3, 4, 44, 55, 66, 77, 88, 99, 112], 4))
