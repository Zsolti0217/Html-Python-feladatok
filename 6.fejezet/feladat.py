from unitTestSaját import teszt

def abszulut_ertek(p):
    """Abszulut érték meghatározása"""
    
    if(p>= 0): return p
    else: return -p
    
#Teszt készlet megadása
teszt(abszulut_ertek(0)==0)
teszt(abszulut_ertek(-1)==1)
teszt(abszulut_ertek(1)==1)
teszt(abszulut_ertek(10)==10)
teszt(abszulut_ertek(-10)==10)
