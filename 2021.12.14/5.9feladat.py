import turtle
def oszlopok(t, magassag):
    if(magassag > 0 ):
        t.begin_fill()           
        t.left(90)
        t.forward(magassag)
        t.write("  "+ str(magassag))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(magassag)
        t.left(90)
        t.penup()
        t.end_fill()             
        t.forward(10)
        t.pendown()
    else:
        t.begin_fill()           
        t.left(90)
        t.forward(magassag)
        t.penup()
        t.forward(-15)
        t.pendown()
        t.write("  "+ str(magassag))
        t.penup()
        t.forward(15)
        t.pendown()
        t.right(90)
        t.forward(40)
        t.penup
        t.right(90)
        t.forward(magassag)
        t.left(90)
        t.penup()
        t.end_fill()             
        t.forward(10)
        t.pendown()
        


a = turtle.Screen()         
a.bgcolor("lightblue")

Eszti = turtle.Turtle()      

Eszti.speed(100)  
Eszti.color("blue", "red")
Eszti.pensize(3)



xs = [48,-117,200,240,-160,260,220]

for S in xs:
    if (S >= 200):
        Eszti.fillcolor("red")
    elif(S >=100 and S < 200):
        Eszti.fillcolor("yellow")
    else:
        Eszti.fillcolor("green")
    oszlopok(Eszti, S)
    
   
a.mainloop()