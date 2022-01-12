szam1 = int(input("Adj meg egy számot! "))
szam2 = int(input("Add meg a második számot! "))

if szam1 > 0 and szam2 > 0:
    print("A két szám közül egyik sme negatív! ")
elif szam1 > 0 and szam2 < 0 :
    print("A két szám közül egyik sem negatív")
elif szam1 < 0 and szam2 > 0:
    print("A klt szám közül az egyik negatív")
elif szam1 