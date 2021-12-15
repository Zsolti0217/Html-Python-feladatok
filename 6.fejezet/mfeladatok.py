napok =["Hétfő" "Kedd" "Szerda" "Csütörtök" "Péntek" "Szombat" "Vasárnap"]
szam = int(input("Adja meg a nap számát 0-6-ig: "))

if(szam == 0):
    print("Hétfő")
    
elif(szam == 1):
    print("Kedd")
    
elif(szam == 2):
    print("Szerda")

elif(szam == 3):
    print("Csütörtök")
    
elif(szam == 4):
    print("Péntek")
    
elif(szam == 5):
    print("Szombat")
    
elif(szam == 6):
    print("Vasárnap")
    
else:
    print("Ilyen nincs.")
        