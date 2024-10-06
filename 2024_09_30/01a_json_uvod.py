import json


# Cteni
with open('absolventi.json', encoding='utf-8') as file:
    absolvents = json.load(file)

print(json)


# Zapis do souboru pomoci metody json.dump()
hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open('hodiny.json', mode='w', encoding='utf-8') as file:
    # Takto ne: slovnik se ulozi jako retezec bez zaruky spravneho JSON formatu
    # print(hours, file=file) 
    
    # Takto ano: metoda json.dump() zajisti spravny format
    # json.dump(hours, file)
    json.dump(hours, file, indent=4)  # Prehledneji formatovany zapis


# Bonus: Ulozeni do retezce v JSON formatu pomoci metody json.dumps()
# json_as_string = json.dumps(hours)
json_as_string = json.dumps(hours, indent=4)
print(json_as_string)


# Zapis s diakritikou v kodovani UTF-8 pomoci parametru ensure_ascii=False
data = {"řeřicha": "Česká Třebová"}

with open("rericha.json", mode="w", encoding="utf-8") as output_file:
    # json.dump(data, output_file)
    json.dump(data, output_file, ensure_ascii=False)