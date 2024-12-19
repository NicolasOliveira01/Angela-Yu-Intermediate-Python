from turtle import Turtle
import random
from scoreboard import Scoreboard


class Food(Turtle): # Food é a subclasse e Turtle é a superclasse
    def __init__(self):
        super().__init__() # Chama o construtor da classe base (Turtle) para inicializar as funcionalidades e atributos dela
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)