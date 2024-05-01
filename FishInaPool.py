# Week5Day2Lesson5 - Three Fish in a Pool
# John Kowal  -  WALTER$

import turtle

def draw_pool(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(size)
    turtle.hideturtle()

def draw_fish(turtle, color, size, x, y):
    turtle.penup()
    turtle.goto(x + 0, y +50)
    turtle.pendown()
    turtle.color(color)
    turtle.left(30)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(120/5.9)
    turtle.penup()
    turtle.goto(x + 110, y + 50)
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
    turtle.goto(x + 25, y + 55)
    turtle.pendown()
    turtle.circle(3)
    turtle.penup()
    turtle.hideturtle()

def main():
    def draw_fishp(turtle):
        turtle.penup()
        turtle.goto(0, 50)
        turtle.pendown()
        draw_fish(turtle, "purple", 30, 0, 30)
        turtle.penup()

    pammy = turtle.Turtle()
    pammy.pensize(3)
    pammy.speed(100)
    draw_fishp(pammy)

    def draw_fishr(turtle):
        turtle.penup()
        turtle.goto(-140, -150)
        turtle.pendown()
        draw_fish(turtle, "red", 30, -140, -150)
        turtle.penup()

    timmy = turtle.Turtle()
    timmy.pensize(3)
    timmy.speed(100)
    draw_fishr(timmy)

    def draw_fishg(turtle):
        turtle.penup()
        turtle.goto(-80, 200)
        turtle.pendown()
        draw_fish(turtle, "green", 30, -80, 160)
        turtle.penup()

    sammy = turtle.Turtle()
    sammy.pensize(3)
    sammy.speed(100)
    draw_fishg(sammy)

tommy = turtle.Turtle()
r = 300
tommy.pensize(10)
tommy.speed(100)
draw_pool(tommy, "blue", r, 0, -300)

main()
turtle.Screen().exitonclick()

