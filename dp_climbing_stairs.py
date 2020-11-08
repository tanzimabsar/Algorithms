from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fib(n)

    def fib(self, n, cache={0: 1, 1: 1}):

        # base case
        if n in cache:
            return cache[n]

        result = self.fib(n - 1, cache) + self.fib(n - 2, cache)
        cache[n] = result

        # if fib(n) can't be found in the cache then add it to the cache, so we never re-calculate the same fib(n) again

        return cache[n]


if __name__ == "__main__":

    s = Solution()
    print(s.climbStairs(1000))
