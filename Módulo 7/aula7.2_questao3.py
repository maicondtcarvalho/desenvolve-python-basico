import re

def eh_palindromo(frase):
    # Remove tudo que não for letra ou número e deixa minúsculo
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
    return frase_limpa == frase_limpa[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if frase.lower() == "fim":
        break
    
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo\n')
    else:
        print(f'"{frase}" não é palíndromo\n')