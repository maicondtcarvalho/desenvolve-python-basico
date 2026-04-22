import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

max_neg = 0
inicio = fim = 0
i = 0

while i < len(lista):
    if lista[i] < 0:
        j = i
        count = 0
        while j < len(lista) and lista[j] < 0:
            count += 1
            j += 1

        if count > max_neg:
            max_neg = count
            inicio = i
            fim = j

        i = j
    else:
        i += 1

del lista[inicio:fim]

print("Editada:", lista)