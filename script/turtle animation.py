import turtle
tut_color=["#FFFF33","#33FF33","#00FFFF","#FF0000","#FF8000","#FF00FF"]
tut=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("#000000")
tut.speed(0)
j=0
for i in range (500):
    while True:
        tut.color(tut_color[j])
        j+=1
        if (j>5):
            j=1
        break
    tut.left(59)
    tut.fd(5+i)
    i+=5
tut.hideturtle()
