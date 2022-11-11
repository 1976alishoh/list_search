def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    max = data[0]
    for i in data :
        if i > max :
            max = i
            
    min = data[0]
    for i in data :
        if i < min :
            min = i
    
    
    return max + min 
print(find_max_min_sum([1, 2, 3, 4, 5]))
print(find_max_min_sum([2, 7, 3, 4, 9]))

