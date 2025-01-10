def add(*args): # aceita uma qtd de variável de argumentos
    #print(args[0])

    total = 0
    for n in args:
        total+=n
    #print(total)

add(4,6,12,6,2,627)

def calculate(n, **kwargs): # ** -> permite passar uma qtd de argumentos nomeados (chave-valor) para uma função, os argumentos são recebidos como um dicionário
    print(kwargs) # {'add': 3, 'multiply': 5}
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5) # n=2

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model") # se esse argumento não for declarado, ele vai retornar none ao invés de crashar
        #self.model = kw["model"] # assim irá crashar se não for passado o argumento
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)