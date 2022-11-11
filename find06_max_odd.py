def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    odd_num = []
    for i in data:
        if i % 2 == 1 and i != 0:
            odd_num = odd_num + [i]
    
    max = odd_num[0]
    for t in odd_num :
        if t > max :
            max = t
    
    return max 
print(find_max_odd([1, 4, 3, 8, 5]))
print(find_max_odd([7, 6, 3, 4, 9]))


