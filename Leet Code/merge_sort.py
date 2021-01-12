def merge_sort(array):

    # divide the list into two parts

    if len(array) > 1:

        middle = len(array) // 2

        left_array = array[:middle]
        right_array = array[middle:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0

        while i < len(left_array) and j < len(right_array):

            if left_array[i] < right_array[i]:
                array[k] = left_array[i]
                i += 1

            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
