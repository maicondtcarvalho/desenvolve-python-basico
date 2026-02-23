genero = input("Digite seu gênero (M ou F): ")
idade = int(input("Digite sua idade: "))
tempo = int(input("Digite seu tempo de serviço (anos): "))

aposentar = (
    (genero == "F" and idade > 60) or
    (genero == "M" and idade > 65) or
    (tempo >= 30) or
    (idade >= 60 and tempo >= 25)
)

print(aposentar)

if aposentar:
    print("Pode se aposentar.")
else:
    print("Não pode se aposentar.")