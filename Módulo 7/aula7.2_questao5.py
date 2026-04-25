import random

def embaralhar_palavras(frase):
    def embaralhar(palavra):
        if len(palavra) <= 3:
            return palavra
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]
    
    return ' '.join(embaralhar(p) for p in frase.split())


# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)