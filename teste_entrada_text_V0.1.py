'''
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45)
[MSC v.1900 32 bit (Intel)] on win32

TESTE DA WIDGET TEXT PARA ENTRADAD DE DADOS.
'''

from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('300x300')
#entrada = ''

text_entrada = Label(text="Entrada*:", fg="blue",font="arial 12")
entrada = Entry(text= "texto",width = 5, font="arial 12")
entrada.pack()


texto = Text(root, height = 4, width = 15)
texto.insert(INSERT, entrada)
texto.pack()

conteudo = texto.get(1.0,END)
print (conteudo)

root.mainloop()
