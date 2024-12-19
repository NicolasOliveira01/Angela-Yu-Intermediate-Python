from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Função com () e sem ():
"""
def saudacao():
    print("Olá!")

def chamar_imediatamente(resultado):
    print("Resultado da função:", resultado)

chamar_imediatamente(saudacao())
# Olá!
# Resultado da função: None
# com (): a função é chamada imediadamente
print("---------------------------")
chamar_imediatamente(saudacao)
# Resultado da função: <function saudacao at 0x000002443F02F160>
# sem (): a função está sendo passada para ser chamada mais tarde
"""

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear_the_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
# so vai chamar a função move_forwards se o espaço for pressionado
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_the_screen)

screen.exitonclick()


