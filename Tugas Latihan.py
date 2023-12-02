print("Nama : Gladis Toti Anggraini ")
print("NIM  : 312310566")
print("==========================")

import math
def a(x):
    return x**2
    a = lambda x: x**2, a
print(a(2))

def b(x, y):
    return math.sqrt(x**2 + y**2)
    b = lambda x, y: x**2 + y**2, b
print(b(2, 4))

def c(*args):
    return sum(args) / len(args)
    c = lambda*args: sum(args) / len(args)
print(c(10, 50))

def d(s):
    return "".join(set(s))
    d = lambda s: "".join(set(s))
print(d("Gladis"))