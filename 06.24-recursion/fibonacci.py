import sys


def fibonacci(n):
    # NOTE: In general, computing a Fibonacci number requires knowing the two
    #       previous Fibonacci numbers:
    #
    # current = previous = None
    #
    # for i in range(n + 1):
    #     print("i: %r, current: %r, previous: %r" % (i, current, previous))
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

    # NOTE: If we instead solve this problem recursively, because the problem
    #       is itself recursively defined, the recursive definition of the
    #       problem tells us the smallest possible problems as well as how to
    #       find smaller versions of the same problem:
    if n == 0:
        print("n: %d, f(n): %d" % (0, 0))
        return 0
    elif n == 1:
        print("n: %d, f(n): %d" % (1, 1))
        return 1
    else:
        print("n: %d, f(n): %d + %d" % (n, fibonacci(n - 1), fibonacci(n - 2)))
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
