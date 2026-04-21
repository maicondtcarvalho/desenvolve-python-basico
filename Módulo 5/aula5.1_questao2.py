import random
import math
n= int (input("Digite a quantidade de números inteiros: "))
soma=0
for i in range(n):
    num= random.randint(0,100)
    print(f"Número {i+1}: {num}")
    soma+=num

    raiz= math.sqrt(soma)
    
print("A soma dos números é:", soma)
print("A raiz quadrada da soma é:", raiz)