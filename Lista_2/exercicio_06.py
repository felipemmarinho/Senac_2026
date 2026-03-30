valor = float(input("digite o valor da compra : "))
if(valor <= 5000):
    novo_valor = valor - (valor * 0.15)
else:
    novo_valor = valor - (valor * 0.20)

print(f'O valor da compra é R$ {novo_valor:.2f}')