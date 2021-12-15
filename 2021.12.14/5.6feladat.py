a= float(input("Adja meg a pontszámot: "))

if(a >= 90 and a <= 100):
    print("Jeles")
elif(a < 90 and a >= 80):
    print("Jó")
elif(a<80 and a>=70):
    print("Közepes")
elif(a<70 and a>=60):
    print("Elégséges")
elif(a < 60 and a > 0):
    print("Elégtelen")
else:
    print("Hülyeség")