# Vozidla hromadné dopravy IDS JMK

# Stáhni si aktuální data o vozidlech IDS JMK z API na adrese 
# https://mapa.idsjmk.cz/api/vehicles.json pomocí modulu `requests`. 

# JSON data ze získané response převeď na slovník. Pozor, načtení pomocí 
# `response.json()` vrací chybu kvůli skrytým nestandardním znakům. 
# Proto na převod použij tento příkaz:
# `data = json.loads(response.content.decode("utf-8-sig"))`

# Kdyby API nefungovalo, načti si místo toho přímo přiložený soubor
#  `vehicles.json` pomocí  with open... a json.load().

# Proveď následující:
# - Spočítej, kolik vozidel je ve slovníku. Seznam vozidel najdeš
#   pod klíčem 'Vehicles'.
# - Spočítej průměrné zpoždění. Informace o zpoždění v minutách najdeš
#   u každého vozidla pod klíčem 'Delay'.
# - Vypiš oba spočítané údaje v pěkném formátu, 
#   např. "V IDS JMK se pohybuje __ vozidel, průměrné zpoždění je __."
#   Bonus: Vypsané zpoždění zaokrouhli na jedno desetinné místo.

# Bonusový úkol:
# - Spočítej podíl nízkopodlažních vozidel z aktuálního celkového počtu vozidel.
#   "Nízkopodlažnost" označuje hodnota true pod klíčem "LF" (low floor).

import requests
import json

url = "https://mapa.idsjmk.cz/api/vehicles.json"

response = requests.get(url)
data_dict = json.loads(response.content.decode("utf-8-sig"))

# Alternativa: nacteni ze souboru
# with open("vehicles.json", mode="r", encoding="utf-8") as file:
#     data_dict = json.load(file)
# ---

# print(data_dict)

number_of_vehicles = len(data_dict['Vehicles'])

delay_total = 0

for vehicle in data_dict['Vehicles']:
    delay_total += vehicle['Delay']

average_delay = delay_total / number_of_vehicles


# # Alternativa: sbírání zpoždění do seznamu
# delays = []

# for vehicle in data_dict['Vehicles']:
#     delays.append(vehicle['Delay'])

# average_delay = sum(delays) / number_of_vehicles


print(f"V IDS JMK se pohybuje {number_of_vehicles} vozidel, průměrné zpoždění je {round(average_delay,1)} minut.")


# Bonusovy ukol:
low_floor_counter = 0

for vehicle in data_dict['Vehicles']:
    is_low_floor = vehicle['LF']
    if is_low_floor:
        low_floor_counter += 1

low_floor_ratio = low_floor_counter / number_of_vehicles

print(f"V IDS JMK se pohybuje {number_of_vehicles} vozidel, z toho je {round(low_floor_ratio*100)} % nízkopodlažních.")
