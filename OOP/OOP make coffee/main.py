# Só foi visto a parte do main.py, os outros arquivos .py já foram dados

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
# report()
# make_payment(cost)
coffee_maker = CoffeeMaker()
# report()
# is_resource_sufficient(drink)
# make_coffee(order)
menu = Menu()
# get_items()
# find_drink(order_name)

# MenuItem()
# name
# cost
# ingredients ({“water”: 100, “coffee”: 16})

is_on = True

while is_on:
    options = menu.get_items() # retorna os coffee diponíveis (latte/espresso/cappuccino/)
    choice = input(f"What would you like ? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()  # qtd de water/milk/coffee na máquina
        money_machine.report()  # dinheiro das vendas dos coffee
    else:
        drink = menu.find_drink(choice) # se for um dos coffee vai retornar um objeto ,MenuItem se não retorna None
        #print(drink)
        if coffee_maker.is_resource_sufficient(drink): # retorna True se tem recursos suficientes e False se não tiver
            if money_machine.make_payment(drink.cost): # drink é um objetvo MenuItem, que tem os atributos name, cost e ingredients
                # make_payment pergunta a qtd de moedas e retorna True se o pagamento foi aceito e False caso contrário
                coffee_maker.make_coffee(drink) # espera um objeto MenuItem (drink)