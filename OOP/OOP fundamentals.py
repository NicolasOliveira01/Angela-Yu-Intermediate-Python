class Test:
    pass #deixa a classe válida mas ela não tem implementação, evitando erros

test_1 = Test()
# uma maneira de criar os atributos, mas vai ter que fazer isso para todos os novos objetos
"""
test_1.id = "001"
test_1.username = "angela"
print(user_1.username)
"""

class User:
    def __init__(self, user_id, username): # construtor da classe
        # self é uma referência ao próprio objeto da classe, muito usado dentro das classes
        #print("new user being created... ")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #

    def follow(self, user): # pede o usuário que vai ser seguido
        user.followers += 1 # o usuário seguido ganha 1 seguidor
        self.following += 1 # o próprio usuário segue mais 1 pessoa

user_1 = User("001", "angela")
user_2 = User("002", "Nicolas")

user_1.follow(user_2)
print(f"user_1.followers: {user_1.followers}")
print(f"user_1.following: {user_1.following}")
print(f"user_2.followers: {user_2.followers}")
print(f"user_2.following: {user_2.following}")