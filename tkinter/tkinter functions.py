from tkinter import *
# https://docs.python.org/3/library/tkinter.html#the-packer
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.htm

window = Tk() # inicializa o ambiente gráfico
window.title("My first GUI Program")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20) # coloca um padding x e y na window

# Label
my_label = Label(text="I'm a Label", font=("Arial", 24)) # aceita argumentos nomeados (chave-valor) (**kwargs)
# diferente de turtle.Turtle() que aceita argumentos posicionais (*args)
my_label.pack() # organizar e posicionar widgets na janela principal
# outras maneiras de definir o text do Label:
my_label["text"] = "New Text"
my_label.config(text="Test")
#my_label.config(padx=10, pady=10)

# PACK / PLACE / GRID são as formas de posicionar e elas não podem se misturar

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text) # muda o text do label

button = Button(text="Click me", command=button_clicked) # sem os () porque está passando a referência da função e não o resultado, com os () chamaria a função imediatamente
button.pack()

# Entry
input = Entry(width=50)
input.pack()
print(input.get()) # obter o valor inserido pelo usuário em um widget Entry
input.insert(END, "Example") # escreve um texto no entry

#Text
text = Text(height=5, width=30)
text.focus() # já coloca o cursor para o usuário já poder digitar direto
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    print(checked_state.get()) # printa 1 se estiver marcado e 0 se não estiver
checked_state = IntVar() # armazena o estado (marcado ou desmarcado)
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get()) # 1 para radiobutton1 e 2 para radiobutton2
radio_state = IntVar() # armazenar o valor da opção selecionada entre os Radiobuttons
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event): # usada quando um item na listbox for selecionado
    print(listbox.get(listbox.curselection())) # imprime o item selecionado da Listbox

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item) # insere cada item na Listbox
listbox.bind("<<ListboxSelect>>", listbox_used) # o item selecionado será impresso
listbox.pack()

window.mainloop() # mantém a janela aberta e fica monitorando interações do usuário, como cliques em botões ou fechamento da janela