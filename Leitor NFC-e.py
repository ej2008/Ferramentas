'''
Leitor NFC-e
'''


from tkinter.filedialog import askopenfile


cabecalho = []
lista = []
colunas = []
item = []
Qtd_itens = 0
Rodape = []

def ler_arquivo():
    try:
        arq = open("NFC_e.txt","r")
        print('Procurando arquivo')
    except FileNotFoundError:
        arq = askopenfile(mode='r', title='Selecione o arquivo para extrair ')
        

    n = 0
    while True:
        l = arq.readline()
        if n <= 4:
            linha = l.strip().split("\t")
            cabecalho.append(linha)

        else:
            ver(cabecalho,"Cabeçalho")
            break
        n += 1

    #l = arq.readline()
    linha = l.strip().split("\t")
    colunas.append(linha)
    ver(colunas,"Colunas")

    n = 1
    p = False
    while True:
        l = arq.readline()
        if "Qtd." not in l and p == False:
            item = l.strip().split("\t")
            item.insert(0,n)
            lista.append(item)
            n += 1

        elif "Qtd." in l and p == False:
            Qtd_itens = l.strip().split("\t")
            p = True

        elif  p == True:
            rodape = l.strip().split("\t")

        else:
            ver(lista,"Itens")
            ver(rodape,"Rodapé")
            break
        
    print("Número :",n -1)



    arq.close()
    
        
def ver(v,o):
    print("+++ %s +++" %o)
    for i in range(len(v)):
        print(v[i])


ler_arquivo()
