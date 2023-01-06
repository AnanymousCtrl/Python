import turtle

ankur1 = [(0, 20), (-80, -60), (-60, -80), (20, 0), (0, 20)]

# Turtle Properties
turtle.hideturtle()
turtle.bgcolor('#00BFFF')  
turtle.setup(400, 400)
turtle.title("MJOLNIR")
ankur1Goto = (0, 20)
turtle.speed(2)

def logo(a, b):
    turtle.penup()
    turtle.goto(b)
    turtle.pendown()
    turtle.color('#969696')
    turtle.begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        turtle.goto(x, y)

    for i in range(len(a[1])):
        x, y = a[1][i]
        turtle.goto(x, y)
    turtle.end_fill()

    
logo(ankur1, ankur1Goto)
turtle.hideturtle()
turtle.done()