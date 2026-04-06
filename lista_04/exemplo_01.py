lista_nomes = []
lista_Familia = []
qtdNomes = 3
qtdFamilia = 2

for familia in range(qtdFamilia):
    for nome in range(qtdNomes):
        nome = input("informe um nome de sua família : ")
        lista_nomes.append(nome)
    lista_Familia.append(lista_nomes)
    lista_nomes = []

for item in lista_Familia :
    print(item)
    print()
