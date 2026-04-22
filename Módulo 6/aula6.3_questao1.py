lista = []

while True:
    n = input("Digite um número (ou 'sair'): ")
    if n.lower() == 'sair':
        if len(lista) >= 4:
            break
        else:
            print("Digite pelo menos 4 números.")
            continue
    lista.append(int(n))

print("Lista original:", lista)
print("3 primeiros:", lista[:3])
print("2 últimos:", lista[-2:])
print("Invertida:", lista[::-1])
print("Índices pares:", lista[::2])
print("Índices ímpares:", lista[1::2])