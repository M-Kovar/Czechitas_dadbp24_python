# Rozcvička
# Vypočti a zobraz cenu jedné noci v hotelu pro zadaný počet osob.
# Cena za noc za osobu je 850 Kč, na počet osob se zeptej uživatele.

price_per_person = 850
persons = int(input("Zadej počet osob: "))

total_price = price_per_person * persons
print(f"Cena za {persons} osob za noc je {total_price} Kč.")