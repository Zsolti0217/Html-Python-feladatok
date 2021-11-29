ak = int(input("Hány óra van:  "))
ker= int(input("hány óra múlva szóljon?:  ") )
if ker < 24 :
    eredm1 = ak + ker
    print(eredm1)
else:
    eredm = ak + (round(ker/24))
    print(eredm)