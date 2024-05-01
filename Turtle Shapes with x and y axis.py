# Week5Day2Lesson3 - Learning Activity - Turtle Class
# John Kowal  -  WALTER$

import turtle

def main():

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

    def draw_square(turtle, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()
        turtle.pendown()

    def draw_pentagon(turtle, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            turtle.left(72)
        turtle.end_fill()
        turtle.pendown()

    def draw_hexagon(turtle, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.begin_fill()
        for i in range(6):
            turtle.forward(size)
            turtle.left(60)
        turtle.end_fill()
        turtle.pendown()

    def draw_septagon(turtle, color, size, x, y):
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.begin_fill()
        for i in range(7):
            turtle.forward(size)
            turtle.left(360/7)
        turtle.end_fill()
        turtle.pendown()

    tommy = turtle.Turtle()
    tommy.shape("turtle")
    tommy.speed(50)

    draw_circle(tommy, "orange", 15, 240, -15)
    tommy.fillcolor("red")

    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.speed(60)

    draw_triangle(timmy, "purple", 30, 200, 25)
    timmy.fillcolor("black")

    pammy = turtle.Turtle()
    pammy.shape("turtle")
    pammy.speed(70)

    draw_square(pammy, "blue", 22.5, 160, 65)
    pammy.fillcolor("green")

    sammy = turtle.Turtle()
    sammy.shape("turtle")
    sammy.speed(80)

    draw_pentagon(sammy, "green", 17.5, 120, 105)
    sammy.fillcolor("blue")

    danny = turtle.Turtle()
    danny.shape("turtle")
    danny.speed(90)

    draw_hexagon(danny, "black", 15, 80, 145)
    danny.fillcolor("purple")

    manny = turtle.Turtle()
    manny.shape("turtle")
    manny.speed(100)

    draw_septagon(manny, "red", 12.5, 40, 185)
    manny.fillcolor("orange")

    tommy = turtle.Turtle()
    tommy.shape("turtle")
    tommy.speed(50)

    draw_circle(tommy, "orange", 15, 0, 225)
    tommy.fillcolor("red")

    manny = turtle.Turtle()
    manny.shape("turtle")
    manny.speed(100)

    draw_septagon(manny, "red", 12.5, -40, 185)
    manny.fillcolor("orange")

    danny = turtle.Turtle()
    danny.shape("turtle")
    danny.speed(90)

    draw_hexagon(danny, "black", 15, -80, 145)
    danny.fillcolor("purple")

    sammy = turtle.Turtle()
    sammy.shape("turtle")
    sammy.speed(80)

    draw_pentagon(sammy, "green", 17.5, -120, 105)
    sammy.fillcolor("blue")

    pammy = turtle.Turtle()
    pammy.shape("turtle")
    pammy.speed(70)

    draw_square(pammy, "blue", 22.5, -160, 65)
    pammy.fillcolor("green")

    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.speed(60)

    draw_triangle(timmy, "purple", 30, -200, 25)
    timmy.fillcolor("black")

    tommy = turtle.Turtle()
    tommy.shape("turtle")
    tommy.speed(50)

    draw_circle(tommy, "orange", 15, -240, -15)
    tommy.fillcolor("red")

    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.speed(60)

    draw_triangle(timmy, "purple", 30, -200, -55)
    timmy.fillcolor("black")

    pammy = turtle.Turtle()
    pammy.shape("turtle")
    pammy.speed(70)

    draw_square(pammy, "blue", 22.5, -160, -95)
    pammy.fillcolor("green")

    sammy = turtle.Turtle()
    sammy.shape("turtle")
    sammy.speed(80)

    draw_pentagon(sammy, "green", 17.5, -120, -135)
    sammy.fillcolor("blue")

    danny = turtle.Turtle()
    danny.shape("turtle")
    danny.speed(90)

    draw_hexagon(danny, "black", 15, -80, -175)
    danny.fillcolor("purple")

    manny = turtle.Turtle()
    manny.shape("turtle")
    manny.speed(100)

    draw_septagon(manny, "red", 12.5, -40, -215)
    manny.fillcolor("orange")

    tommy = turtle.Turtle()
    tommy.shape("turtle")
    tommy.speed(50)

    draw_circle(tommy, "orange", 15, 0, -255)
    tommy.fillcolor("red")

    manny = turtle.Turtle()
    manny.shape("turtle")
    manny.speed(100)

    draw_septagon(manny, "red", 12.5, 40, -215)
    manny.fillcolor("orange")

    danny = turtle.Turtle()
    danny.shape("turtle")
    danny.speed(90)

    draw_hexagon(danny, "black", 15, 80, -175)
    danny.fillcolor("purple")

    sammy = turtle.Turtle()
    sammy.shape("turtle")
    sammy.speed(80)

    draw_pentagon(sammy, "green", 17.5, 120, -135)
    sammy.fillcolor("blue")

    pammy = turtle.Turtle()
    pammy.shape("turtle")
    pammy.speed(70)

    draw_square(pammy, "blue", 22.5, 160, -95)
    pammy.fillcolor("green")

    timmy = turtle.Turtle()
    timmy.shape("turtle")
    timmy.speed(60)

    draw_triangle(timmy, "purple", 30, 200, -55)
    timmy.fillcolor("black")

main()

turtle.hideturtle()
turtle.speed(0)

turtle.pendown()
turtle.forward(300)
turtle.back(300)
turtle.pendown()
turtle.left(90)
turtle.forward(300)
turtle.back(300)
turtle.pendown()
turtle.left(90)
turtle.forward(300)
turtle.back(300)
turtle.pendown()
turtle.left(90)
turtle.forward(300)
turtle.back(300)

turtle.exitonclick()