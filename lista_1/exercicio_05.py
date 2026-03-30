import math
vlr_aplicacao = float(input('Digite o valor da aplicação mesal : '))
taxa = float(input('digite o valor da taxa :'))
meses = int(input('digite a quantidade de meses :'))

vlr_acumulado = (vlr_aplicacao * (1+taxa) * math.sqrt(meses))/taxa

print(f'O valor acumulado é {vlr_acumulado:.2f}')

