import random
import pandas

# List Comprehension
# [new_item for item in list if test]

name = "Nicolas"
new_list = [letter for letter in name]

range_list = [e*2 for e in range(1,5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) > 5]

# ----------------------------------------------------------------------------------------------------------
# Dictionary Comprehension
# {new_key: new_value for (key, value) in dictionary.items()}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student:random.randint(1, 100) for student in names}
#print(students_scores)
passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
#print(passed_students)

# ----------------------------------------------------------------------------------------------------------

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split() # cada palavra é um elemento da lista
result = {word: len(word) for word in words} # chave é a palavra e seu valor é a quantidade de letras
#print(result)

# ----------------------------------------------------------------------------------------------------------

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {key: (value*9/5) + 32 for (key, value) in weather_c.items()}

#print(weather_f)

# ----------------------------------------------------------------------------------------------------------

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# looping through dictionaries:
for (key, value) in student_dict.items(): # .items() faz uma tupla com a chave e o valor -> ('student', ['Angela', 'James', 'Lily'])
    #print(f"{key}: {value}")
    pass

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows(): # iterrows() usado para iterar sobre as linhas de um df
    #print(index) # os índices do df
    #print(row) # mostra as linhas do df
    if row.student == "Angela":
        #print(row.score)
        pass
# ----------------------------------------------------------------------------------------------------------

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row["letter"]: row["code"] for (index, row) in nato.iterrows()} # as letras são as chaves e as palavras são os valores

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
