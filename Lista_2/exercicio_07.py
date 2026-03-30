total = float(input('Digite o valor de suas vendas :'))
if(total >= 20000):
    print(f'O seu salário é de R$ {total*0.20:.2f}')
else:
    print(f'O seu salario é de R$ {total*0.15:.2f}')