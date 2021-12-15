#1. Az égtájak rövid néven:"É" "K" "NY" "D"
#Írjunk programot "(fordulj_orajarasi_iranyba()" névvel,
# ami a paramétereként megadott égtáj után következik. 
# Rossz paraméter esetén None értéket ad vissza
def fordulj_orajarasi_iranyba(p): 
    if (p== "É"): return "K"
    if (p== "K"): return "D"
    if (p== "D"): return "NY"
    if (p== "NY"): return "É"
    return None

#2 
def nap_nev(k):
    if(k == 0): return "Hétfő"
    elif(k== 1): return "Kedd"
    elif(k== 2): return "Szerda"
    elif(k== 3): return "Csütörtök"
    elif(k== 4): return "Péntek"
    elif(k== 5): return "Szombat"
    elif(k== 6): return "Vasárnap"
    return None
   
   




