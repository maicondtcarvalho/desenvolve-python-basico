cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

# remove pontos e traço
cpf = cpf.replace(".", "").replace("-", "")

# verifica se tem 11 dígitos e se são números
if len(cpf) != 11 or not cpf.isdigit():
    print("Inválido")
else:
    # evita CPFs com todos os números iguais (ex: 11111111111)
    if cpf == cpf[0] * 11:
        print("Inválido")
    else:
        # cálculo do primeiro dígito
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        
        resto = soma % 11
        if resto < 2:
            dig1 = 0
        else:
            dig1 = 11 - resto

        # cálculo do segundo dígito
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        
        resto = soma % 11
        if resto < 2:
            dig2 = 0
        else:
            dig2 = 11 - resto

        # validação final
        if cpf[9] == str(dig1) and cpf[10] == str(dig2):
            print("Válido")
        else:
            print("Inválido")