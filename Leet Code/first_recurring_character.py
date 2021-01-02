""" Default value are None if keys are not found """


def return_first_recurring_character(array):

    results = {}
    for i in array:
        if i in results:
            return results.get(i)
        else:
            results[i] = i


print(return_first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(return_first_recurring_character([2, 3, 4, 5]))
