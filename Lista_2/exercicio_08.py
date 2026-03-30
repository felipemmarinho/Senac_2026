nome_1 = input('Digite o nome do 1º vendedor')
vlr_venda_1 = float(input('Digite o valor de suas vendas'))

nome_2 = input('Digite o nome do 2º vendedor')
vlr_venda_2 = float(input('Digite o valor de suas vendas'))

nome_3 = input('Digite o nome do 1º vendedor')
vlr_venda_3 = float(input('Digite o valor de suas vendas'))

if(vlr_venda_1 > 50000):
    comissao_1 = vlr_venda_1 * 12.5
elif (vlr_venda_1 <= 30000 and vlr_venda_1 >= 50000 ):
    comissao_1 = vlr_venda_1 *9.5
else:
    comissao_1 = vlr_venda_1 *7.0

if(vlr_venda_2 > 50000):
    comissao_2 = vlr_venda_2 * 12.5
elif (vlr_venda_2 <= 30000 and vlr_venda_2 >= 50000 ):
    comissao_2 = vlr_venda_2 * 9.5
else:
    comissao_2 = vlr_venda_2 * 7.0

if(vlr_venda_3 > 50000):
    comissao_3 = vlr_venda_3 * 12.5
elif (vlr_venda_3 <= 30000 and vlr_venda_3 >= 50000 ):
    comissao_3 = vlr_venda_3 * 9.5
else:
    comissao_3 = vlr_venda_3 * 7.0
total_vendas = vlr_venda_1+vlr_venda_2+vlr_venda_3

print(f"O vendedor {nome_1}, vendeu R$ {vlr_venda_1:.2f} e sua comissão é de R$ {comissao_1:.2f}")
print(f"O vendedor {nome_2}, vendeu R$ {vlr_venda_2:.2f} e sua comissão é de R$ {comissao_2:.2f}")
print(f"O vendedor {nome_3}, vendeu R$ {vlr_venda_3:.2f} e sua comissão é de R$ {comissao_3:.2f}")
print(f"O total de vendas da empresa é de R$ {total_vendas:.2f}")


