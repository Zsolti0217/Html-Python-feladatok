import math
a = int(input("Írjon be egy számot: "))
b = int(input("Írjon be egy számot: "))
def atfogo(a,b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c

print(atfogo(a,b))