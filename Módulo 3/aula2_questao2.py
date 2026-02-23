Person1=int(input('Digite a idade da pessoa 1:'))
Person2=int(input('Digite a idade da pessoa 2:'))

pode_entrar=(Person1>17) or (Person2>17)

print(pode_entrar)

if pode_entrar:
    print('As duas pessoas podem entrar na festa.')
else:
    print('As duas pessoas não podem entrar na festa.')