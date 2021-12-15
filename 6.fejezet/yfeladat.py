szam = int(input())

def paratlan_e(szam):
    if(szam % 2 == 0):
        return False
    else:
        return True
    
print(paratlan_e(szam))