from tkinter import *
from tkinter import ttk

#cores
cor1 = "#0d0c0c" #preto
cor2 = "#f7f7f5" #branco
cor3 = "#040959" #azul
cor4 = "#474242" #cinza
cor5 = "#f59025" #laranja

#Tela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variável todos valores

todos_valores = ''

#função
def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)


    #valor na tela
    valor_texto.set(todos_valores)

#Calcular
def calculos():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)

#Apagar
def apagar():
    global todos_valores
    todos_valores = ''
    valor_texto.set("")

#label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg= cor2)
app_label.place(x=0, y=0)

#Criando Botão

b_1 = Button(frame_corpo, command=apagar, text="C", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)

b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0)

b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=51)

b_5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=51)

b_6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=51)

b_7 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=51)

b_8 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=103)


b_9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=103)

b_10 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=103)

b_11 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=103)

b_12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=155)

b_13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=155)

b_14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=155)

b_14 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=180, y=155)

b_15 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=0, y=208)

b_12 = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=120, y=208)

b_12 = Button(frame_corpo, command=calculos, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=180, y=208)




janela.mainloop()


