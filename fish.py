# Fish
# John Kowal  -  WALTER$

import turtle

def draw_arc(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(30)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(120/5.9)
    turtle.penup()
    turtle.goto(110, 50)
    turtle.left(70)
    turtle.pendown()
    turtle.forward(31)
    turtle.right(110)
    turtle.forward(30)
    turtle.right(110)
    turtle.forward(31)
    turtle.left(50)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(120/5.9)
    turtle.penup()
    turtle.goto(25, 55)
    turtle.pendown()
    turtle.circle(3)

    turtle.hideturtle()

def draw_fishp(turtle):
    draw_arc(turtle, "pink", 30, 0, 50)

tammy = turtle.Turtle()
tammy.pensize(3)
tammy.speed(100)
draw_fishp(tammy)

turtle.Screen().exitonclick()