total_cliente = int(input('Digite o total de clientes que compraram: '))

clientes = []   # lista de dicionários
valor_total = 0

for i in range(total_cliente):
    nome = input("Digite o seu nome: ")
    compra = float(input("Digite o valor de sua compra: "))

    if compra <= 250:
        desconto = compra * 0.15
    else:
        desconto = compra * 0.20

    valor_final = compra - desconto
    valor_total += valor_final

    # cria um dicionário para o cliente
    cliente = {
        "nome": nome,
        "valor_compra": compra,
        "desconto": desconto,
        "valor_final": valor_final
    }

    clientes.append(cliente)

# Exibir resultados
for c in clientes:
    print(f'O cliente {c["nome"]} comprou R${c["valor_compra"]:.2f}, '
          f'obteve R${c["desconto"]:.2f} de desconto e pagará R${c["valor_final"]:.2f}')

print(f'A empresa arrecadou um total de R${valor_total:.2f}')
