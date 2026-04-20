n=int(input("Digite o valor de n: "))
cont=1
soma=0
while cont <= n:
    idade= int(input("Qual a sua idade? "))
    soma= soma + idade
    cont= cont + 1
print("A média de idade é:", soma/n)
print(f"A média das idades é {soma/n:.0f} anos.")