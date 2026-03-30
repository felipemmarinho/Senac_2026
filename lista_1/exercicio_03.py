vlr_produto = float(input('Digite o valor do produto : '))
desconto = vlr_produto - (vlr_produto * 0.9)
novo_valor = vlr_produto - desconto
print(f'O valor do desconto de 9% é {desconto}, com isso o produto ficou no valor de : R$ {novo_valor}')