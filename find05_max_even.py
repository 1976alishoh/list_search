def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    even_num = []
    for i in data:
        if i % 2 == 0:
            even_num = even_num + [i]
    
    max = even_num[0]
    for i in even_num :
        if i > max :
            max = i
    
    return max 
print(find_max_even([1, 4, 3, 8, 5]))
print(find_max_even([7, 6, 3, 4, 9]))


