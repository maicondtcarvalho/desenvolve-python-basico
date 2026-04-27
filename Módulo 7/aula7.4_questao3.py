arquivo = open("estomago.txt", "r", encoding="utf-8")
linhas = arquivo.readlines()
arquivo.close()

print("Primeiras 25 linhas:\n")

for i in range(25):
    if i < len(linhas):
        print(linhas[i], end="")

print("\n\nNúmero de linhas:", len(linhas))

maior_linha = ""

for linha in linhas:
    if len(linha) > len(maior_linha):
        maior_linha = linha

print("\nLinha com maior número de caracteres:")
print(maior_linha)

contador_nonato = 0
contador_iria = 0

for linha in linhas:
    texto_limpo = ""

    for letra in linha:
        if letra.isalpha() or letra == "í" or letra == "Í":
            texto_limpo += letra.lower()
        else:
            texto_limpo += " "

    palavras = texto_limpo.split()

    for palavra in palavras:
        if palavra == "nonato":
            contador_nonato += 1
        if palavra == "íria":
            contador_iria += 1

print("\nMenções a Nonato:", contador_nonato)
print("Menções a Íria:", contador_iria)