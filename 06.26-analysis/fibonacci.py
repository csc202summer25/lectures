import sys


def fibonacci(n):
    # NOTE: To compute, for example, f_5, we have to know f_4 and f_3. To
    #       compute f_4, we then have to know f_3 and f_2 -- this means we end
    #       up naively having to compute f_3 *twice*. Doing work recursively is
    #       fine; doing the same work multiple times is not.
    if n == 0:
        return None, 0
    elif n == 1:
        return 0, 1
    else:
        previous, current = fibonacci(n - 1)
        return current, current + previous 
