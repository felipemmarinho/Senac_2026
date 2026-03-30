produto_1 = input("Digite o 1º produto : ")
estoque_1 = int(input('Digite a quantidade em estoque : '))


produto_2 = input("Digite o 2º produto : ")
estoque_2 = int(input('Digite a quantidade em estoque : '))

produto_3 = input("Digite o 3º produto : ")
estoque_3 = int(input('Digite a quantidade em estoque : '))

produto_4 = input("Digite o 4º produto : ")
estoque_4 = int(input('Digite a quantidade em estoque : '))

if estoque_1 < 30:
    print(f"o produto {produto_1} está com o estoque abaixo do permitido")
if estoque_2 < 30:
    print(f"o produto {produto_2} está com o estoque abaixo do permitido")
if estoque_3 < 30:
    print(f"o produto {produto_3} está com o estoque abaixo do permitido")
if estoque_4 < 30:
    print(f"o produto {produto_4} está com o estoque abaixo do permitido")

