def total_price(persons, breakfast=False):
    cena_za_noc = 850
    cena_za_snidani = 125

    celkem = cena_za_noc * persons

    if breakfast:
        # ... neni potreba psat <if breakfast == True>
        # ... a else vetev taky ne
        celkem += cena_za_snidani * persons

    return celkem


print(f'Cena za tři lidi: {total_price(3)}')

# print(f'Cena za dva lidi se snídaní: {total_price(2, True)}')
print(f'Cena za dva lidi se snídaní: {total_price(2, breakfast=True)}')