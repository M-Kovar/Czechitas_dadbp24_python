# Želva

# Pokud už všechno umíš, nemáš co dělat a nudíš se, vyzkoušej Želvu:
# https://docs.python.org/3/library/turtle.html
# Želva umí kreslit. Pomocí ovládání směru jejího pohybu a dalších parametrů
# můžeš tvořit obrázky a zkoušet si, jak želva reaguje na pokyny.

# Vyzkoušej si pár pokynů podle tutoriálu.
# Po spuštění kódu by se mělo otevřít nové okno, ve kterém bude želva kreslit.

# 1. První ukázka
# import turtle as t

# # Volba parametrů vykreslování
# t.shape("turtle")
# t.speed(3)

# # Vykreslení čtyřhranného obrazce for cyklem
# num_levels = 5
# for i in range(num_levels * 4): 
#     t.forward(i * 5)
#     t.right(90)

# # Zajistí zobrazení okna, dokud ho uživatel sám nezavře
# t.done()


# 2. Objektově-orientované želvy
import turtle as t
import random

t1 = t.Turtle()
t1.shape("turtle")
t1.speed(5)

t2 = t.Turtle()
t2.shape("circle")
t2.speed(5)

for i in range(100):
    steps = int(random.random() * 100)
    angle = int(random.random() * 360)

    t1.right(angle)
    t1.forward(steps)

    t2.left(angle)
    t2.forward(steps)

t1.done()
t2.done()