nome_praia = ''
qtde_distancia_centro = 0
qtde_media_veranista = 0
soma_veranista = 0
nome_distancia = []


while nome_praia == 'fim':
    nome_praia = input("Digite o nome da praia : ")
    distancia_centro = float(input('Qual a distância da praia para ocentro : '))
    num_medio_veranista = int(input("Qual o número médio de veranista : "))
    tipo_acesso = int(input('Qual o tipo de acesso à praia, 0 para acesso não asfaltado e 1 para asfaltado'))

    if distancia_centro > 15:
        qtde_distancia_centro += 1

    if tipo_acesso == 0:
        qtde_media_veranista += num_medio_veranista
        soma_veranista += 1

    if ((num_medio_veranista < 1000) and (tipo_acesso == 1)):
        praia = {
            'nome' : nome_praia,
            'distancia' : distancia_centro 
        }
        nome_distancia.append(praia)

print(f'O número de praias distante mais que 15 km é {qtde_distancia_centro}')
print(f'A quantidade média de veranista nas praias nessa última temporada é {qtde_media_veranista/soma_veranista}')
for i in len(nome_distancia):
    

            
        


        









 




    
