produto1=input('Digite o nome do produto 1:')
preço1=float(input('Digite o preço do produto 1:'))
qtde1=int(input('Digite a QTDE do produto 1:'))

produto2=input('Digite o nome do produto 2:')
preço2= float(input('Digite o preço do produto 2:'))
qtde2=int(input('Digite a QTDE do produto 2:'))

produto3=input('Digite o nome do produto 3:')
preço3=float(input('Digite o preço do produto 3:'))
qtde3=int(input('Digite a QTDE do produto 3:'))

print('Saída')
print(f'Total: {(preço1*qtde1)+(preço2*qtde2)+(preço3*qtde3):,.2f}')