def max_element(lst):
    temp = None
    for element in lst:
        if temp is None or element > temp:
            temp = element
    return temp


print(max_element([2, -1, 9, 8, 5, -3, 0, 8]))
