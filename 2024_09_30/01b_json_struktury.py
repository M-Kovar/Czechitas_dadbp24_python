import json

with open('zavod.json', encoding='utf-8') as file:
    runners = json.load(file)

print(runners)


# Pokusy s indexovanim
print(runners[0]['jmeno'])
print(runners[-1]['casy']['1.kolo'])

casy_prvnich_kol = []

for runner in runners:
    casy_prvnich_kol.append(runner['casy']['1.kolo'])

print(casy_prvnich_kol)