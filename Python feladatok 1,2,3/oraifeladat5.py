c = 10000 
r = 0.08
m = 12
t = int(input("évek száma"))
t = int(t)

fv = c* (1 + r / m) ** (m * t)
print("A betét értéke a futam idő végén",fv)
