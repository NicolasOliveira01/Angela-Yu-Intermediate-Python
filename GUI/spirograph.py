import turtle
from turtle import Turtle, Screen
from random import randint

tim = Turtle()
turtle.colormode(255)

def random_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirografh(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirografh(5)

screen = Screen()
screen.exitonclick()