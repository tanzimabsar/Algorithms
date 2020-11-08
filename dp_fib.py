def fib(n):

    memo = {}

    def fibm(n):

        if memo.get(n):
            return memo[n]

        if n < 2:
            return n

        else:
            memo[n] = fib(n - 1) + fib(n - 2)
            return memo[n]

    return fibm(n)


print(fib(35))


def fib_old(n):

    if n < 2:
        return n

    return fib_old(n - 1) + fib_old(n - 2)


print(fib_old(35))
