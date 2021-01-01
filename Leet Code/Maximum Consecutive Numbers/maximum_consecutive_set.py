def findMax(numbers, n):
    setNumbers = set(numbers)
    ans = 0
    for i in range(n):
        if numbers[i] in setNumbers:
            j = numbers[i]

            while j in setNumbers:
                j += 1

            ans = max(ans, j - numbers[i])

    return ans


if __name__ == "__main__":
    print(findMax([1, 94, 93, 1000, 5, 92, 73], 3))
