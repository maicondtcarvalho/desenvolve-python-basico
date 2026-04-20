n=int(input("Digite a quantidade de experimentos: "))
cont=0
soma_sapo=0
soma_rato=0
soma_coelho=0
while cont < n:
    print(cont, n)
    quantia=int(input("Digite a quantidade de cobaias: "))
    tipo=input("Qual o tipo de cobaia? (C, R ou S) ")
    if tipo == "C":
        soma_coelho+= quantia
    elif tipo == "R":
        soma_rato+= quantia
    elif tipo == "S":
        soma_sapo+= quantia

    cont+= 1
print("Total de Cobaias: ", soma_sapo + soma_rato + soma_coelho)
print("Total de Sapos: ", soma_sapo)
print("Total de Ratos: ", soma_rato)
print("Total de Coelho: ", soma_coelho)
