from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9 # vai reduzir em 10% a velocidade da bola, isso porque time.sleep(), quanto menor o parãmetro, maior a velocidade

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1 # quando alguém fizer ponto vai voltar para a velocidade inicial da bola
        self.bounce_x() # a bola recomeça indo para a pessoa que ganhou o ponto