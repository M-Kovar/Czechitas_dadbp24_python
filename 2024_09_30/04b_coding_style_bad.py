# Bad example: cteni tohoto kodu zpusobuje bolest hlavy

from random import randrange as rr
def gen_sec():
  s = ''
  while len(s) < 4:
   d = str(rr(0, 10))
   if d in s:
    continue
   s += d
  return s
out = gen_sec()
print(out)
print(out[0])
print(out[-1])
