pares = [x for x in range(20, 51) if x % 2 == 0]

quadrados = [x**2 for x in [1,2,3,4,5,6,7,8,9]]

div7 = [x for x in range(1, 101) if x % 7 == 0]

par_impar = ["par" if x % 2 == 0 else "impar" for x in range(0, 30, 3)]

print("Pares:", pares)
print("Quadrados:", quadrados)
print("Divisíveis por 7:", div7)
print("Par/Ímpar:", par_impar)