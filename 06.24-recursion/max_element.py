def max_element(lst):
    """
    Find the largest element in a list.

    :param lst: A list of comparable elements
    :return: The largest element in that list, or None if empty
    """
    
    # NOTE: Iteration is the repeated application of a procedure. Here, the
    #       function "iterates over" the elements within a list:
    #
    # temp = None
    # for element in lst:
    #     if temp is None or element > temp:
    #         temp = element
    # return temp

    # NOTE: A function should solve a problem -- it should take as argument(s)
    #       an instance of the problem, and it should produce as return value
    #       a solution to that problem. Here, the list of integers is the
    #       problem, and the largest integer in that list is the solution. A
    #       recursive function calls itself, thus, a recursive function must
    #       within itself solve the *same problem*.

    # NOTE: One or more base cases should solve the smallest versions of the
    #       problem non-recursively. Here, the smallest possible lists are the
    #       lists of zero or one elements:
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]

    # NOTE: One or more recursive cases should address larger versions of the
    #       problem by reducing them to smaller versions of the *same problem*.
    #       Here, the problem is a list, thus, a smaller version of the same
    #       problem is a shorter list containing some of the same elements:
    return max(lst[0], max_element(lst[1:]))


print(max_element([2, -1, 9, 8, 5, -3, 0, 8]))
