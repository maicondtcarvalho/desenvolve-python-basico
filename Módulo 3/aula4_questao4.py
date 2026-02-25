distancia_km=float(input("Digite a distância em km: "))
peso_kg=float(input("Digite o peso em kg: "))

if distancia_km<=100:
    valor=peso_kg*1
elif distancia_km>100 and distancia_km<=300:
    valor=peso_kg*1.5
elif distancia_km>300:
    valor=peso_kg*2

if peso_kg>10:
    valor=valor+10
    print(f"O valor do frete é R$ {valor:,.2f} reais")
else:    
    print(f"O valor do frete é R$ {valor:,.2f} reais")
print("Fim do programa")




#distancia_km=float(input("Digite a distância em km: "))
#peso_kg=float(input("Digite o peso em kg: "))
#if distancia_km<=100:
#    print(f"O valor do frete é R$ {peso_kg*1:,.2f} reais")
#elif distancia_km>100 and distancia_km<=300:
#    print(f"O valor do frete é R$ {peso_kg*1.5:,.2f} reais")
#elif distancia_km>300:
#    print(f"O valor do frete é R$ {peso_kg*2:,.2f} reais")
#print("Fim do programa")