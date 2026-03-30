soma_positivo = 0
qtde_negativa = 0


for contador in range(5):
    numero_inteiro = int(input('informe um número : '))
    if numero_inteiro >= 0:
        soma_positivo = soma_positivo + numero_inteiro
    else:
        qtde_negativa = qtde_negativa + 1
print('A  soma dos valores positivos é {0}'.format(soma_positivo))
print(f'A soma dos valores positivos é {qtde_negativa}')