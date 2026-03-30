numero = 87
soma = 0
pares = []

while numero <= 907:
    if numero % 2 == 0:
        pares.append(numero)

    soma += numero
    numero += 1
print('Os números pares entre 87 e 907 são' )

for i in range(len(pares)):
    print(pares[i])

print(f'A soma dos números entre 87 e 907 é : {soma}')    

     