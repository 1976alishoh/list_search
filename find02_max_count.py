def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    sanoq = 0
    max = data[0]
    for i in data :
        if i > max :
            max = i
            
    for  i in data :
        if i == max:
           sanoq = sanoq + 1
    return sanoq
print(find_max_count([1, 8, 3, 8, 5]))
print(find_max_count([13, 8, 3, 4, 9]))
