# "Necista" funkce - vyuziva globalni promenne -> tohle nechceme delat
exchange_rate = 26

def convert_to_euro(crown):
    return crown * exchange_rate

print(convert_to_euro(100))
# print(crown)


# Pass: funkce bez kodu
def code_me_later(par1, par2):
    # TODO: Finalize this function
    pass