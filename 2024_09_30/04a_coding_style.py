# Instalace nastroje autopep8 v terminalu: pip install autopep8

# Volani v terminalu:
# autopep8 <nazev_souboru.py>       ... Vypise upraveny soubor do terminalu
# autopep8 <nazev_souboru.py> -i    ... Prepise puvodni soubor upravenym

from random import randrange


def generate():
    '''Generate a 4-digit secret number. The digits must be all different.'''
    secret = ''

    while len(secret) < 4:
        digit = str(randrange(0, 10))
        if digit in secret:
            continue
        secret += digit

    return secret


number = generate()
print(number)
print(number[0])  # first digit
print(number[-1])  # last digit
