""" Traverse the list, and find the smallest item then sqap the index at possition 1 """


def selection_sort(array, smallest=None):

    for i in range(0, len(array)):

        minimum = i

        for j in range(i + 1, len(array)):
            if array[minimum] > array[j]:

                minimum = j

        array[minimum], array[i] = array[i], array[minimum]

    return array


print(selection_sort([1, 2, 3, 4, 5, 3, 4, 2, 1]))
