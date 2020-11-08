import math


def divide_and_conquer(iterable):

    if iterable == []:
        return 0
    else:
        return iterable[0] + sum(iterable[1:])


def count(iterable):

    if iterable == []:
        return 0
    else:
        return 1 + count(iterable[1:])


def fib_memo(n):

    memo = [None] * 100

    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n] == 0 or memo[n] is None:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(13), fib_memo(13))
