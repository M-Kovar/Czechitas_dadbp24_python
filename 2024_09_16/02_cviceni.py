#  Cviceni 1

def mult(a, b):
    # vysledek = a * b
    # return vysledek
    return a * b

result = mult(5, 2)
print(result)


# Cviceni 2

def kilometers_to_miles(kilometers):
    # 1 mile is cca 1.609 km
    return kilometers / 1.609

def miles_to_kilometers(miles):
    # 1 mile is cca 1.609 km
    return miles * 1.609


print(kilometers_to_miles(100))
print(miles_to_kilometers(100))

# ---

def celsius_to_fahrenheit(temperature_celsius):
    temperature_fahrenheit = (9 * temperature_celsius / 5) + 32
    return temperature_fahrenheit

def fahrenheit_to_celsius(temperature_fahrenheit):
    temperature_celsius = 5 * (temperature_fahrenheit - 32) / 9
    return temperature_celsius


celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

fahrenheit_temp = 77
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is equal to {celsius_temp}°C")


# Bonus: Cviceni 3

def ramecek(slovo):
    delka = len(slovo)
    sirka_ramecku = delka + 4  # chceme trochu mista kolem slova
    print('*' * sirka_ramecku)
    print(f'* {slovo} *')
    print('*' * sirka_ramecku)

# znak ramecku muze byt nepovinnym parametrem - viz prislusna kapitola
def ramecek(slovo, znak_ramecku="*"):
    delka = len(slovo)
    sirka_ramecku = delka + 4  # chceme trochu mista kolem slova
    print(znak_ramecku * sirka_ramecku)
    print(f'{znak_ramecku} {slovo} {znak_ramecku}')
    print(znak_ramecku * sirka_ramecku)


ramecek("PYTHON")
ramecek("PYTHON", "-")


def mult(a, b):
    result = a * b
    return result