cim = input("Adja meg a könyv címét")
oldal = int(input("Adja meg az oldalainak számát "))

def konyv(oldalak):
    if oldalak > 150:
        return True
    else:
        return False
 
cim = (input("Add meg a könyv címét"))   
while cim:
    oldalak = int(input("Add meg az oldalainak számát "))
    konyv(oldalak)
    if oldalak == True:
        print(cim, "hosszú terjedelmű könyv")
    else:
        print(cim, "rövid terjedelmű a könyv")
    cim = (input("Add meg a könyv címet"))
    