'''
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45)
[MSC v.1900 32 bit (Intel)] on win32

TESTE DA WIDGET TEXT PARA ENTRADAD DE DADOS.
'''

from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('300x300')




texto = Text(root, height = 4, width = 15)
texto.insert(INSERT, input('digite seu texto :'))
texto.pack()

conteudo = texto.get(1.0,END)
print (conteudo)

root.mainloop()
