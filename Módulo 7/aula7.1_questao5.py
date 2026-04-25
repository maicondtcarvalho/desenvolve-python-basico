frase = input("Digite uma frase: ")

vogais = "aeiou"
indices = []

for i, letra in enumerate(frase.lower()):
    if letra in vogais:
        indices.append(i)

print(len(indices), "vogais")
print("Índices", indices)