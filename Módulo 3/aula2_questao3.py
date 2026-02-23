idade = int(input("Digite sua idade: "))

jogou_3 = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ")
jogou_3 = jogou_3 == "True"

vitorias = int(input("Quantos jogos já venceu? "))

apto = (16 <= idade <= 18) and jogou_3 and (vitorias >= 1)

print("Apto para ingressar no clube de jogos de tabuleiro:", apto)