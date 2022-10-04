import turtle

# Screen
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.title("Flamengo")

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.color("Green")
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(50)
turtle.setheading(-10)
turtle.forward(200)
turtle.setheading(195)
turtle.forward(200)
turtle.end_fill()

turtle.penup()
turtle.goto(-150, 50)
turtle.pendown()
turtle.color("Yellow")
turtle.begin_fill()
turtle.setheading(90)
turtle.forward(50)
turtle.setheading(-10)
turtle.forward(500)
turtle.setheading(195)
turtle.forward(500)
turtle.end_fill()

turtle.done()
