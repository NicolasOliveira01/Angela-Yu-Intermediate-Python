from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)# Controla a atualização da tela e 0 desativa totalmente as animações, no caso seria para a cobra mover por inteira e tirar a animação de cada parte da
# cobra de mexer individualmente

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")


game_is_on = True
while game_is_on:
    screen.update() #força a atualização da tela quando ela está com a atualização desativada (tracer(0)), assim todas as partes da cobra vão andar e so no final vai atualizar
    time.sleep(0.1) # introduz uma pausa de 0,1 segundo em cada iteração do laço
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15: # se a cabeça da cobra estiver em uma distância menor de 15 da comida
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with all
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()