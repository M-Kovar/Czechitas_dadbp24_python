# Instalace modulu v terminalu: 
# pip install requests ..nebo.. python -m pip install requests

import requests

# (HTTP request lze pouzit obecne na jakoukoliv URL)
response = requests.get('https://kodim.cz')
print(response)    # Response object ... HTTP status code 200 "OK" znamena uspesny request
print(response.content)

# Zadost o JSON a jeho ulozeni do promenne
response = requests.get('https://api.kodim.cz/python-data/people')
print(response.content)
data = response.json()
print(data)