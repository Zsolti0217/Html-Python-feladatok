import random
class nev:
    def __init__(self, name, gender, work):
        self.name =name
        self.gender = gender
        self.work = work
        self.randomszam = random.randint(1, 50)
        
    def nem(self):
        if self.gender == "f":
            return "férfi"
        elif self.gender == "n":
            return "nő"
        
    def veletlen(self):
        return random.randint(1, 50)

    def kiirat(self):
        return "{neve} egy {munka} {nem} volt, szerencse száma a {rdm.}. ".format(neve = self.name, munka = self.work, nem = self.nem(), rdm=self.veletlen())


ember1 = nev(input("Add meg a neved"), input("Add meg a nemét (f/n)"), input("kérem a munkáját"))
ember2 = nev(input("Add meg a neved"), input("Add meg a nemét (f/n)"), input("kérem a munkáját"))
ember3 = nev(input("Add meg a neved"), input("Add meg a nemét (f/n)"), input("kérem a munkáját"))

lista = [ember1, ember2, ember3]

e1 = ember1.kiirat()
print(e1)
e2 = ember2.kiirat()
print(e2)
e3 = ember3.kiirat()
print(e3)

x = open("születettki.txt", "w")
x.write(e1)
x.writelines("/n")
x.write(e2)
x.writelines("/n")
x.write(e3)
x.writelines("/n")
x.close()
