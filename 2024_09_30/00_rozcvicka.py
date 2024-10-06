# Rozcvička

# Vytvoř slovník se dvěma páry "klíč: hodnota" libovolného obsahu 
# a ulož ho do proměnné. Pomocí klíče přistup k hodnotě jednoho ze dvou záznamů
# a ulož ji do textového souboru.


dictionary = {
    "zvire": "kapybara", 
    "prezdivka": "přerostlé morče"
    }

# Alternativa pro definovani slovniku:
# dictionary = dict()
# dictionary["zvire"] = "kapybara"
# dictionary["prezdivka"] = "přerostlé morče"
# ---

value = dictionary["prezdivka"]
print(value)

with open('output.txt', mode='w', encoding="utf-8") as file:
    print(value, file=file)