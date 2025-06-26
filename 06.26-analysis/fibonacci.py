import sys


def fibonacci(n):
    # current = previous = None
    #
    # for i in range(n + 1):
    #     if i == 0:
    #         current = 0
    #     elif i == 1:
    #         previous = current
    #         current = 1
    #     else:
    #         temp = previous
    #         previous = current
    #         current = current + temp
    #
    # return current

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
