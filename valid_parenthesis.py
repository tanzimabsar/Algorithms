from collections import deque


def isValid(s: str) -> bool:
    stack = deque()

    for letter in s:

        if letter == "(" or letter == "{" or letter == "[":
            stack.appendleft(letter)

        if letter == "(" and stack[-1] == ")":
            stack.pop()

    return len(stack)


print(isValid("()"))
