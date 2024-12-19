from turtle import Screen, Turtle
import time # permite trabalhar com datas, medir intervalos e pausar a execução do programa

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Controla a atualização da tela e 0 desativa totalmente as animações, no caso seria para a cobra mover por inteira e tirar a animação de cada parte da
# cobra de mexer individualmente

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()  #força a atualização da tela quando ela está com a atualização desativada (tracer(0)), assim todas as partes da cobra vão andar e so no final vai atualizar
    time.sleep(0.1) # introduz uma pausa de 0,1 segundo em cada iteração do laço

    for seg_num in range(len(segments)-1, 0, -1): # start(tamanho da lista -1), stop(antes de chegar a 0, não inclui 0), step (ir de -1 a -1)
        # a ideia desse for é começar pelo último objeto da cobra e não chegar até o primeiro, para fazer a cobra conseguir virar e andar por total
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        # armazena as coordenadas do elemento anterior do elemento que está em análise, se o elemento de índice 10 está em análise vai ser o elemento de índice 9
        segments[seg_num].goto(new_x, new_y) # move o elemento em análise para a posição do elemento anterior, ficando "em cima" dele
    segments[0].forward(20) # move somente o primeiro elemento, para que os elementos de trás os acompanhe
    segments[0].left(90) # sempre o primeiro elemento que vai guiar os demais

screen.exitonclick()