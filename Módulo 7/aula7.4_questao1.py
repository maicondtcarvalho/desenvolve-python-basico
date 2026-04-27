import os

frase = input("Digite uma frase: ")

caminho_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho_script, "frase.txt")

arquivo = open(caminho_arquivo, "w", encoding="utf-8")
arquivo.write(frase)
arquivo.close()

print("Frase salva em", caminho_arquivo)