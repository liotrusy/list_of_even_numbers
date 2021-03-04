# final version
def generate_list(start, end):
    """Returns a list of even numbers."""
    if start < end:
        even_numbers_list = [x for x in range(start, end) if x % 2 == 0]
        return even_numbers_list
    else:
        raise ValueError(f"{start} is not smaller than {end}.")