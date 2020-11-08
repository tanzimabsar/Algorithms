import math


class Solution:
    def climbStairs(self, n: int) -> int:

        ways = 0

        for x in range(n + 1):

            for y in range(0, n + 1, 2):

                if x + y == n:

                    steps = x + int(0.5 * y)
                    ways += math.factorial(steps) / (
                        (math.factorial(x)) * (math.factorial(steps - x))
                    )

        return int(ways)


if __name__ == "__main__":

    s = Solution()
    print(s.climbStairs(1000))
