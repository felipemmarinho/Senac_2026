distancia = float(input('Digite a distância entra as cidades : '))
velocidade = float(input('Qual a sua velocidade em km/h : '))

tempo = distancia/velocidade
metros_segundos = velocidade/3.6

print(f'O tempo gasto no percurso é de {tempo:.2f} ')
print(f'E sua velocidade em metros/segundos é  {metros_segundos:.2f} ')

