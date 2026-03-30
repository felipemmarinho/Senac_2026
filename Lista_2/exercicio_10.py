num_1 = float(input("Digite o 1º número : "))
num_2 = float(input("Digite o 2º número : "))
num_3 = float(input("Digite o 3º número : "))

maior = 0
menor = 99999999999999999999

if num_1 > maior:
    maior = num_1
if num_2 > maior:
    maior = num_2
if num_3 > maior:
    maior = num_3

if num_1 < menor:
    menor = num_1
if num_2 < menor:
    menor = num_2
if num_3 < menor:
    menor = num_3

print(f"O maior número é : {maior}, e o menor é {menor}")
