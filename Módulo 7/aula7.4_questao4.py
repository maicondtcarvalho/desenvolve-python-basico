import random

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

arquivo = open("gabarito_forca.txt", "r", encoding="utf-8")
palavras = arquivo.read().splitlines()
arquivo.close()

palavra_secreta = random.choice(palavras).lower()

arquivo = open("gabarito_enforcado.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()

partes = conteudo.split("=========")

estagios = []

for parte in partes:
    parte = parte.strip()
    
    if parte != "":
        estagios.append(parte + "\n=========")

progresso = []

for letra in palavra_secreta:
    progresso.append("_")

erros = 0
letras_tentadas = []

print("JOGO DA FORCA")

while erros < 6 and "_" in progresso:
    print("\nPalavra:", " ".join(progresso))
    
    tentativa = input("Digite uma letra: ").lower()

    if tentativa in letras_tentadas:
        print("Você já tentou essa letra.")
        continue

    letras_tentadas.append(tentativa)

    if tentativa in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == tentativa:
                progresso[i] = tentativa
    else:
        erros += 1
        imprime_enforcado(erros, estagios)

if "_" not in progresso:
    print("\nParabéns! Você acertou a palavra:", palavra_secreta)
else:
    print("\nVocê perdeu! A palavra era:", palavra_secreta)