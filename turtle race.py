from turtle import Turtle, Screen
from random import choice


screen = Screen()
screen.setup(500, 400) # define o tamanho da screen
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
objects = []

for _ in range(6):
    turtle = Turtle(shape="turtle")
    objects.append(turtle)

for e in range(len(objects)):
    objects[e].color(colors[e])

y_initial = -80
for e in objects:
    e.penup()
    e.goto(x=-230, y = y_initial)
    y_initial += 30

def forward():
    speed = [3, 8, 10, 3]
    x = choice(speed)
    return x

def check_x():
    for e in range(len(objects)):
        x = objects[e].position()[0]
        if x > 120:
            return False
        else:
            return True

def who_won_the_race():
    index = 0
    bigger = 0
    for e in range(len(objects)):
        turtle_index = objects[e].position()[0]
        if objects[e].position()[0] > bigger:
            bigger = turtle_index
            index = e
    return index

while check_x():
    for e in objects:
        x = forward()
        e.forward(x)
index_winning_turtle = who_won_the_race()
if user_bet == colors[index_winning_turtle]:
    print("You win")
else:
    print(f"You lost, {colors[index_winning_turtle]} won the race")

screen.exitonclick()