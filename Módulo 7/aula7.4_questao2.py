import os

caminho_script = os.path.dirname(os.path.abspath(__file__))

arquivo_entrada = open(os.path.join(caminho_script, "frase.txt"), "r", encoding="utf-8")
texto = arquivo_entrada.read()
arquivo_entrada.close()

palavra = ""
palavras = []

for letra in texto:
    if letra.isalpha():
        palavra += letra
    else:
        if palavra != "":
            palavras.append(palavra)
            palavra = ""

if palavra != "":
    palavras.append(palavra)

arquivo_saida = open(os.path.join(caminho_script, "palavras.txt"), "w", encoding="utf-8")

for p in palavras:
    arquivo_saida.write(p + "\n")

arquivo_saida.close()

arquivo_saida = open(os.path.join(caminho_script, "palavras.txt"), "r", encoding="utf-8")

print(arquivo_saida.read())

arquivo_saida.close()