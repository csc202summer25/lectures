import sys


def fibonacci(n):
    current = previous = None

    for i in range(n + 1):
        if i == 0:
            current = 0
        elif i == 1:
            previous = current
            current = 1
        else:
            temp = previous
            previous = current
            current = current + temp

    return current


print(fibonacci(5))
