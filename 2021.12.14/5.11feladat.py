a = int(input("Adjon meg egy értéket: "))
b = int(input("Adjon meg egy értéket: "))
c = int(input("Adjon meg egy értéket: "))
def derekszogu(a,b,c):
    derekszog =False 
    
    oldalak = [a,b,c]
    print(oldalak)
    
    oldalak.sort
    print(oldalak)
    
    oldalak[0] *= oldalak[0]
    oldalak[1] *= oldalak[1]
    oldalak[2] *= oldalak[2]
    print(oldalak)
    
    if(oldalak[0] + oldalak[1] == oldalak[2]):
        derekszog = True
        return derekszog
    
print(derekszogu(a,b,c))
