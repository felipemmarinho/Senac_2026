soma_positivo = 0
qtde_negativa = 0
lista_numero = []

for i in range(5):
    numero_inteiro = int(input('Digite o seu número'))
    lista_numero.append(numero_inteiro)

    #append = inclui no final da list
    #insert = coloca num determinado índice da lista

for numero_inteiro in lista_numero:
    if numero_inteiro >= 0:
        soma_positivo = soma_positivo + numero_inteiro
    else:
        qtde_negativa = qtde_negativa + 1

print(f'A soma dos números positivos é : {soma_positivo}')
print('A quantidade de números negativos{0} '.format(qtde_negativa))