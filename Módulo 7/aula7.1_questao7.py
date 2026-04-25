import random

def encrypt(lista):
    n = random.randint(1, 10)
    resultado = []

    for nome in lista:
        novo = ""
        for c in nome:
            codigo = ord(c)
            if 33 <= codigo <= 126:
                novo += chr(33 + (codigo - 33 + n) % 94)
            else:
                novo += c
        resultado.append(novo)

    return resultado, n


entrada = input("Digite os nomes separados por vírgula: ")
nomes = [nome.strip() for nome in entrada.split(",")]

nomes_cript, chave = encrypt(nomes)

print("Chave:", chave)
print("Nomes criptografados:", nomes_cript)