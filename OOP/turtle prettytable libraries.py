# Using turtle graphic
# https://docs.python.org/3/library/turtle.html
"""from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle") # transforma em uma tartaruga
timmy.color("chocolate4") # muda a cor
timmy.forward(100)

my_screen = Screen() # janela que a turtle vai aparecer
print(my_screen.canvheight) # canvheight é o atributo (características ou propriedades de um objeto) do objeto my_screen
my_screen.exitonclick() # a janela só vai fechar quando tiver um click"""

# Using prettytable
# https://pypi.org/project/prettytable/

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])
table.align = "l"

print(table)
