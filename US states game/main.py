import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) # coloca a imagem


data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title() # title() deixa a primeira letra maiúscula

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        #print(new_data)
        new_data.to_csv("states_to_learn.csv") # arquivo csv que tem todos os estados que não foram escritos
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(state_data["x"].item(), state_data["y"].item()) # item() pega o valor único da Series e converte em int ou float
        # Esse é o retorno sem o item():
        """9
           182
           Name: x, dtype: int64"""
        t.write(answer_state)
