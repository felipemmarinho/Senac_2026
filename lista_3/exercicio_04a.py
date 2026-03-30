total_clientes = int(input('Quantidade de clientes : '))
clientes = []
valor_empresa = 0

for i in range(total_clientes):
    nome = input('Digite o nome do cliente : ')
    valor_compra = float(input('digite o valor da compra : '))

    if valor_compra <= 250:
        desconto = valor_compra * 0.15
    else:
        desconto = valor_compra * 0.20
    
    valor_liquido   = valor_compra - desconto

    valor_empresa += valor_liquido

    cliente = {
        "nome" : nome,
        "valor_compra" : valor_compra,
        "desconto" : desconto,
        "total_pagar" : valor_liquido,
    }
    clientes.append(cliente)
    
for c in clientes:
    print(f'O cliente {c["nome"]} comprou R${c["valor_compra"]:.2f} reais e obteve R${c["desconto"]:.2f} reais de desconto e sua conta ficou em R${c['total_pagar']:.2f} reais')

print(f'A empresa lucrou R${valor_empresa:.2f} reais')