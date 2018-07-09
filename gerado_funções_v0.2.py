'''
Use para gerar funões apartir de listas

entrada:
lista = 'nome','telefone','email','data' 
entrada = 'entrada_'


saida:
self.entrada_nome.delete(0, 'end')
self.entrada_telefone.delete(0, 'end')
self.entrada_email.delete(0, 'end')
self.entrada_data.delete(0, 'end')
'''

lista = ('id', 'data', 'nome', 'telefone', 'celular', 'email', 'endereco', 'nr_res',
                'bairro', 'cidade', 'estado', 'cep', 'camisa', 'tipo_sanguineo', 'fator_fh','co_piloto', 'jeep_club', 'veiculo',
                'placa', 'cnh', 'cat_principal', 'sub_categoria', 'pneu', 'obs','apelido')

entrada = "entrada_"
original = entrada

for i in range(len(lista)):
    entrada +=lista[i]
    print("self.{} [{}]= linha[{}]".format(entrada,"\"text\"",i))
    entrada = original
    
'''
for i in range(len(lista)):
    entrada +=lista[i]
    print("""self.%s["text"]= %s"""%entrada,lista[i])
    entrada = original
    
'''

'''
#entrada = str(input())
#original = entrada
#lista = []


while True:
    l =  input()
    if l == "parar":
        break
    lista.append(l)
    
print()

for i in range(len(lista)):
    entrada +=lista[i]
    print("self.%s.delete(0, 'end')"%entrada)
    entrada = original
    
print()
'''
