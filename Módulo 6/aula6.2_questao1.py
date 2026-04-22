import random

lista = [random.randint(-100, 100) for _ in range(20)]
lista_ordenada = sorted(lista)

print("Lista ordenada:")
print(lista_ordenada)

print("\nLista original:")
print(lista)

indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

print("\nÍndice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)