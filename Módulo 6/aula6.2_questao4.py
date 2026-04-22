lista1 = []
lista2 = []

n1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {n1} elementos da lista 1:")
for _ in range(n1):
    lista1.append(int(input()))

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {n2} elementos da lista 2:")
for _ in range(n2):
    lista2.append(int(input()))

resultado = []

i = 0
while i < len(lista1) and i < len(lista2):
    resultado.append(lista1[i])
    resultado.append(lista2[i])
    i += 1

# adiciona os elementos restantes da maior lista
resultado.extend(lista1[i:])
resultado.extend(lista2[i:])

print("Lista intercalada:", *resultado)