def generate_list_version_1():
    """Returns a list of even numbers. First version"""
    even_numbers_list = []
    for number in range(1, 11):
        if number % 2 == 0:
            even_numbers_list.append(number)
    return even_numbers_list