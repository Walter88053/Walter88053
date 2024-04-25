# Week5Day2Lesson2 - Put Turtle Graphics Anywhere on the Web
# John Kowal  -  WALTER$

import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

def draw_triangle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 0, 0)
draw_circle(tommy, "blue", 50, 125, 0)
draw_circle(tommy, "yellow", 50, 250, 0)
tommy.fillcolor("red")

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.speed(500)

draw_triangle(timmy, "green", 100, -50, 100)
draw_triangle(timmy, "blue", 100, 75, 100)
draw_triangle(timmy, "yellow", 100, 200, 100)
timmy.fillcolor("black")

turtle.exitonclick()
