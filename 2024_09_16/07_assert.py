def sum_two_numbers(a, b):
    return a + b

def sum_two_numbers__incorrect(a, b):
    return a * b


value1 = sum_two_numbers(2, 3)
assert value1 == 5, "Sum of 2 a 3 should be 5"

value2 = sum_two_numbers__incorrect(2, 3)
assert value2 == 5, "Sum of 2 a 3 should be 5"