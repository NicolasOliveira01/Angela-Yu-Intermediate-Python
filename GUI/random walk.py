import turtle
from turtle import Turtle, Screen
from random import choice, randint

t = Turtle()
t.hideturtle()
t.speed(0)
t.pensize(10)

turtle.colormode(255)

def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(500):
    angles = [0, 90, 180, 270, 360]
    for _ in range(5):
        t.pencolor(random_colors())
        angle = choice(angles)
        angles.remove(angle)
        t.right(angle)
        t.forward(20)

screen = Screen()
screen.exitonclick()