import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")

    heiny = turtle.Turtle()
    heiny.shape("turtle")
    heiny.color("blue")
    heiny.speed(1)
    draw_square(heiny)

    queenie = turtle.Turtle()
    queenie.shape("arrow")
    queenie.color("red")
    queenie.circle(100)
    queenie.speed(1)

    window.exitonclick()

draw_art()
