import turtle

# movement of turtle
ankur1 =[[(0, 100), (50, 100), (50,50), (0, 50), (50, 0)]]
ankur2 =[[(150, 100), (100, 100), (200, 100)]]

# Turtle Properties
turtle.hideturtle()
turtle.bgcolor('#760c10')  # up marron
turtle.setup(500, 600)
turtle.title("logo checkup")
ankur1Goto = (0, 0)
ankur2Goto = (150, 0)
turtle.speed(1)

def logo(a, b):
    turtle.penup()
    turtle.goto(b)
    turtle.pendown()
    turtle.color('#d7bb2b') # Mettalic Gold
    turtle.begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        turtle.goto(x, y)

# Final Finishing
logo(ankur1, ankur1Goto)
logo(ankur2, ankur2Goto)
turtle.hideturtle()
turtle.done()