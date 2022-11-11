def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    sanoq = 0
    min = data[0]
    for i in data :
        if i < min :
            min = i
    
    for  i in data :
        if i == min:
           sanoq = sanoq + 1
    return sanoq
print(find_min_count([1, 8, 3, 8, 5]))
print(find_min_count([0, -4, 3, 9, -2, -4]))


