comprimento = int(input("Qual é o comprimento do terreno? "))  # Lê o comprimento do terreno
largura = int(input("Qual é a largura do terreno? "))  # Lê a largura do terreno
preco_m2 = float(input("Qual é o preço do metro quadrado? "))  # Lê o preço do metro quadrado

area_m2 = comprimento * largura  # Calcula a área do terreno
preco_total = preco_m2 * area_m2  # Calcula o valor total do terreno

print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")  # Exibe o resultado formatado