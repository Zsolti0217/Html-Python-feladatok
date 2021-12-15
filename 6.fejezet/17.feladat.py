t = int(input())
n = int(input())

def tobbszoros_e(t,e):
    if(t % n == 0):
        return "Többszöröse"
    else:
        "Nme többszöröse"
        
print(tobbszoros_e(t, n))