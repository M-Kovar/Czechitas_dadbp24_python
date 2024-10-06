## Cviceni 2

import requests

url = "https://svatky.adresa.info/json"


# Ukol 1
response = requests.get(url)
namesday_today = response.json()
print(namesday_today)


# Ukol 2
day = input("Zadej den (DD): ")
month = input("Zadej měsíc (MM): ")

url_with_date = f"{url}?date={day}{month}"

response = requests.get(url_with_date)
namesday_on_date = response.json()
print(namesday_on_date)


# Ukol 3
response = requests.get(url, params={"date": f"{day}{month}"})
namesday_on_date = response.json()
print(namesday_on_date)