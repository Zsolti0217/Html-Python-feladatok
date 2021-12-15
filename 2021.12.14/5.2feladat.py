napok =["Hétfő", "Kedd" ,"Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
indulasi_nap = int(input("Melyik napon indultál (0-6)"))
eltelt_nap = int(input("Hány nap telt el?"))

def szamitas(napok, indulasi_nap, eltelt_nap):
    for i in napok:
        a= (indulasi_nap + eltelt_nap) % 7
        return napok[a]
    
print(szamitas(napok, indulasi_nap, eltelt_nap))