import turtle
from turtle import Turtle, Screen
from random import choice

import colorgram

colors = colorgram.extract('image.jpg', 40)

#print(colors[0])
# <colorgram.py Color: Rgb(r=253, g=251, b=247)
#print(colors[0].rgb)
# Rgb(r=253, g=251, b=247)
#print(colors[0].rgb.r)
# 253

"""rgb_colors = []

for e in colors:
    r = e.rgb.r
    g = e.rgb.g
    b = e.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)"""

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.hideturtle()

def make_circle(color):
    tim.color(color)
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()

tim.penup()
tim.left(180)
tim.forward(400)
tim.left(90)
tim.forward(320)
tim.left(90)
tim.forward(150)
tim.pendown()

index_colors = [i for i in range(len(color_list))]

for i in range(1, 11):
    for e in range(1, 11):
        if len(index_colors) == 0:
            original_index_colors = [i for i in range(len(color_list))]
            index_colors = original_index_colors
        color = choice(index_colors)
        index_colors.remove(color)
        make_circle(color_list[color])
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)
    tim.pendown()

screen = Screen()
screen.exitonclick()


