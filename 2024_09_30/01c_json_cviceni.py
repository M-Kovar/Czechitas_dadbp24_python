# Zavod

import json

with open('zavod.json', mode="r", encoding='utf-8') as file:
    runners = json.load(file)

finishers = []

for runner in runners:
    if runner['casy']['oficialni'] != 'DNF':
        finishers.append(runner['jmeno'])

print(finishers)
print(finishers[1])