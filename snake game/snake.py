from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position()) # passa a posição do úlimo (-1) objeto da cobra

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start(tamanho da lista -1), stop(antes de chegar a 0, não inclui 0), step (ir de -1 a -1)
            # a ideia desse for é começar pelo último objeto da cobra e não chegar até o primeiro, para fazer a cobra conseguir virar e andar por total
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # armazena as coordenadas do elemento anterior do elemento que está em análise, se o elemento de índice 10 está em análise vai ser o elemento de índice 9
            self.segments[seg_num].goto(new_x, new_y)  # move o elemento em análise para a posição do elemento anterior, ficando "em cima" dele
        self.head.forward(MOVE_DISTANCE)  # move somente o primeiro elemento, para que os elementos de trás os acompanhe

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

