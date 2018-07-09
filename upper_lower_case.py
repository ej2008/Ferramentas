


linha = (8, '10/03/2018', 'Francinaldo Moreira', '(80)3040-4555', '', 'fm@mail.com',
         '15', '98', 'Sul', 'Salgado', 'AM', '848448-999', 'GG', '', '', 'Serra', 'Moto ',
         'DFF-5059', 86984940, '', 'Nacional', 'Normal', '', 'Morro', '')


op = str(input('''Digite ''upper'' ou ''lower :'''))

if op == 'upper':
    for i in range(len(linha)):
        if type(linha[i]) == str:
            print(linha[i].upper())

if op == 'lower':
    for i in range(len(linha)):
        if type(linha[i]) == str:
            print(linha[i].lower())

