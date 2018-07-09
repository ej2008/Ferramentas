'''
Rotina retirado do site python-brasil postado por: 
Sobrinhos Tia Dani <sobrinhostiadani@gmail.com>
Está rotina é para adequar o separador da casa decimal "." para "," usada no Brasil)
'''

import locale


print(locale.setlocale(locale.LC_ALL,""))

while True:
    try:
        a=float(input("Digite um valor ou 0 para sair: "))
        if a == 0: break
    
        print(a)

        #print(locale.setlocale(locale.LC_ALL,""))    

        print(locale.format("%.3f", a, grouping= True))

        print(locale.currency(a,grouping=True))
        
    except ValueError:
        print("Utilize o \".\" como separador da casa decimal!") 
    
    
            
