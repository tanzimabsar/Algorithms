def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        print(i)
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort([1, 4, 5, 6, 7, 8, 33, 31, 5]))
