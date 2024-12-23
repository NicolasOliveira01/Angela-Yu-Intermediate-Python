from turtle import Turtle

ALIGMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read()) # o high_score é o número que está no txt e é preciso abrir o txt para acessar ele
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=('Courier', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score: # se a pontuação atual for maior que o high_score, o high_score se torna a pontuação atual
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}") # substitui o valor do txt para o high_score atual
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()