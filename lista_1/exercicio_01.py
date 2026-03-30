numero_1 = float(input('Digite o primeiro número : '))
numero_2 = float(input('Digite o segundo número : '))
numero_3 = float(input('Digite o terceiro número : '))
numero_4 = float(input('Digite o quarto número : '))

peso_1 = 1
peso_2 = 2
peso_3 = 3
peso_4 = 4

media = (numero_1 * peso_1)+(numero_2 * peso_2)+(numero_3 * peso_3)+(numero_4 * peso_4)/(peso_1+peso_2+peso_3+peso_4)

print(f"A média ponderada dos números {numero_1}+{numero_2}+{numero_3}+{numero_4} é : {media}")