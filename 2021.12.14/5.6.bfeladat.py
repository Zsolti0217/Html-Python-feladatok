xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in xs:
    if(i >= 90 and i <= 100):
        print("Jeles")
    elif(i < 90 and i >= 80):
        print("Jó")
    elif(i<80 and i>=70):
        print("Közepes")
    elif(i<70 and i>=60):
        print("Elégséges")
    elif(i < 60 and i >= 0):
        print("Elégtelen")
    else:
        print("Hülyeség")