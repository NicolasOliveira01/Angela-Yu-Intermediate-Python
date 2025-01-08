import pandas
# https://pandas.pydata.org/docs/

data = pandas.read_csv("weather_data.csv")
#print(type(data)) DataFrame -> planilha
#print(type(data["temp"])) # Series -> coluna (lista)

data_dict = data.to_dict() # faz um dicionário que cada coluna do df é um dicionário que tem os índices como chave e seus respectivos valores
#print(data_dict)

temp_list = data["temp"].to_list() # coloca os valores de "temp" em uma lista
# [12, 14, 15, 14, 21, 22, 24]

data["temp"].mean() # faz a média
data["temp"].max() # retorna o valor máximo

# data["condition"] tem o mesmo resultado de data.condition

monday = data["day"] == "Monday" # retornar a linha (row)
#print(monday)

max_temp = data[data["temp"] == data["temp"].max()] # mostra a linha que possui a maior temp
#print(max_temp)

monday_condition = data[data["day"] == "Monday"]["condition"] # retorna o valor de "condition" onde "day" é igual a "condition"
#print(monday_condition)

temp_monday = data[data["day"] == "Monday"]["temp"][0] # 12
fahrenheit = (temp_monday * 1.8) + 32

data_dict1 = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}

data1 = pandas.DataFrame(data_dict1) # transforma em um df
data1.to_csv("new_data.csv") # faz um arquivo csv e pede um nome para este arquivo