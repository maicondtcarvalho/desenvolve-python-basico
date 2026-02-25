Nota_filme=int(input("Digite a nota do filme: "))
print("A nota do filme é: ", Nota_filme)
if Nota_filme==5:
    print(f"O filme é excelente")
elif Nota_filme==4:
    print(f"O filme é bom")
elif Nota_filme==3:
    print(f"O filme é regular")
elif Nota_filme==2:
    print(f"O filme é ruim")
elif Nota_filme==1:
    print(f"O filme é péssimo")
else:
    print(f"Nota inválida")
print("Fim do programa")