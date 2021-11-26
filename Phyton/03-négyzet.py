import turtle
def negyzet_rajzolás(toll, hossz):
    """Egy h oldalú négyzet rajzolása"""
    for i in range(4):
        toll.forward(hossz)
        toll.left(90)


# Egy ablak létrehozása és néhány tulajdonság beállítása
a = turtle.Screen()
a.bgcolor("light")
a.title("Négyzet rajzolása")

# Rajzeszköz létrehozása és rajzolás
toll = turtle.Turtle()
negyzet_rajzolas(toll, 50)
 #Ablak bezárása 
 a.mainloop()