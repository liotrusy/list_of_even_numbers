def generate_list_version_1():
    """Returns a list of even numbers. First version"""
    even_numbers_list = []
    for number in range(1, 11):
        if number % 2 == 0:
            even_numbers_list.append(number)
    return even_numbers_list

def generate_list_version_2():
    """Returns a list of even numbers. Second version"""
    even_numbers_list = [x for x in range(1, 11) if x % 2 == 0]
    return even_numbers_list

def generate_list_version_3():
    """Returns a list of even numbers. Third version"""
    even_numbers_list = []
    for number in range(2, 11, 2):
        even_numbers_list.append(number)
    return even_numbers_list

def generate_list_version_4():
    """Returns a list of even numbers. Second version"""
    even_numbers_list = [x for x in range(2, 11, 2)]
    return even_numbers_list