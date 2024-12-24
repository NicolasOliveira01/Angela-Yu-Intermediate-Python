#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
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