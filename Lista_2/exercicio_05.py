salario = float(input('Digite o seu salário'))

if(salario <= 500):
    print('isento')
elif(salario < 500 and salario <= 1500 ):
    print('O desconto é de 10%')
elif(salario < 1500 and salario <= 2500):
    print('O desconto é de 15%')
else:
    print('Seu desconto é de 20%')