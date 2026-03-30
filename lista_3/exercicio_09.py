diarias = int(input("Digite o total de diárias : "))

valor_estadia = 0

if diarias < 15 :
    valor_estadia = (150*diarias) + (8*diarias)
elif diarias == 15 :
    valor_estadia = (150*diarias) + (6.30*diarias)
else:
    valor_estadia = (150*diarias) + (5*diarias)    

print(f"A sua conta ficou em R${valor_estadia:.2f}")
    