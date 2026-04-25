nome=str(input("Digite um nome: "))

for i in range(len(nome)):
    print(nome[:i+1])

print("O nome digitado foi:", nome)

