# Želva

# Pokud už všechno umíš, nemáš co dělat a nudíš se, vyzkoušej Želvu:
# https://docs.python.org/3/library/turtle.html
# Želva umí kreslit. Pomocí ovládání směru jejího pohybu a dalších parametrů
# můžeš tvořit obrázky a zkoušet si, jak želva reaguje na pokyny.

# Vyzkoušej si pár pokynů podle tutoriálu.
# Po spuštění kódu by se mělo otevřít nové okno, ve kterém bude želva kreslit.

# 1. První ukázka
import turtle as t

# # Volba parametrů vykreslování
t.shape("turtle")
t.speed(3)


# # Vykreslení čtyřhranného obrazce for cyklem
num_levels = 5
for i in range(num_levels * 4): 
    t.forward(i * 5)
    t.right(90)

# # Zajistí zobrazení okna, dokud ho uživatel sám nezavře
t.done()
