from typing import List

""" Assume that the array is already sorted and then halve the list """


def binary_search(array, element, start, end):

    if start > end:
        # In this case we know that the array is not valid
        return None

    # find the middle
    mid = (start + end) // 2

    # if the element you are trying to find is in that middle index return the index
    # this is the case that it is trying to find
    if element == array[mid]:
        return mid

    # if it is list then at that index, recursively call binary search
    # but the last index is one less than the mid point

    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)

        # otherwise start on the second half because you know it lies on that side

    else:
        return binary_search(array, element, mid + 1, end)


print(binary_search([1, 2, 3, 4, 5], 5, 1, 5))
