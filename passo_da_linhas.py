l = int(input("Qtd de linhas: "))
r =  int(input("Qtd de linhas de recuo: "))
nl =int(input("Qtd de número de linhas: "))
 
for i in range(nl):
    p = r + ((l-r)//nl) * i
    print (p)

