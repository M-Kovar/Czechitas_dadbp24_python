def get_mark(points, bonus=0):
    # Pokud nezadame 'bonus' jako argument, pouzije se vychozi hodnota 0
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark


points = 65
bonus = 20

mark1 = get_mark(points, bonus)
mark2 = get_mark(points)

print(mark1)
print(mark2)


# Argumenty lze predavat i pojmenovanim
mark = get_mark(points=65, bonus=20)

# ... nebo takto (parametr a argument stejny nazev mit nemusi, ale muze)
mark = get_mark(points=points, bonus=bonus)


# Funkce round jako dalsi priklad
print(round(23.86576))
print(round(23.86576, 2))
print(round(23.86576, -1))