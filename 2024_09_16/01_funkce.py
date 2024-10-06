# Definice funkce
def greet_user(name):
    print(f"Ahoj {name}!")

greet_user("Jirko")


# Return: vraceni hodnoty
def sum_two_numbers(a, b):
    # result = a + b
    # return result
    return a + b

def sum_three_numbers(a, b, c):
    return a + b + c


returned_value = sum_two_numbers(5, 3)
print(returned_value)

returned_value2 = sum_three_numbers(5, 3, 2)
print(returned_value2)


# Print versus return
greeting = greet_user("Jirko")
print(greeting)     # Funkce nic nevraci (pouze printuje na obrazovku), resp. vraci None (prazdny datovy typ)

returned_value = sum_two_numbers(5, 3)
print(returned_value)   # Funkce vraci vysledek operace skrz return