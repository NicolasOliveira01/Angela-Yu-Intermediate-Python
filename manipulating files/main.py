#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""with open("./Input/Names/invited_names.txt", mode="r") as file:
    names_original = file.readlines()
names = []
for e in names_original:
    right_name = e.strip()
    names.append(right_name)

with open(f"./Input/Letters/starting_letter.txt", mode="r") as file:
    contents = file.read()
for e in names:
    with open(f"./Output/ReadyToSend/letter_for{e}.txt", mode="w") as file2:
        x = contents.replace("[name]", e)
        file2.write(x)"""

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines() # transforma cada linha em um elemento de uma lista (contando os \n)
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() # armazena a carta inteira
    for name in names:
        stripped_name = name.strip() # tira os espaços iniciais e finais
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) # troca "[name]" pelo nome em análise
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter: # cria um arquivo txt com o nome para cada pessoa
            completed_letter.write(new_letter)