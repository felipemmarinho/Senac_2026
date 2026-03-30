total_alunos = int(input('Digite o total de alunos pesquisados : '))
alunos = []
media_altura = 0
media_idade = 0
contador_altura = 0
contador_idade = 0

#a)  Idade média dos alunos com altura menor que 1,70 m; 
# b) A altura média dos alunos com mais de vinte anos

for i in range(total_alunos):
    idade = int(input('Digite a sua idade : '))
    altura = float(input('Digite a sua altura : '))

    aluno = {
        "altura" : altura,
        "idade" : idade,
    }
    alunos.append(aluno)

for c in alunos:
    if c["idade"] > 20 :
        media_altura += altura
        contador_altura += 1

    if c["altura"] < 1.70 :
        media_idade += idade
        contador_idade += 1

print(f'A idade média dos alunos com altura menor que 1.70 é : {media_idade/contador_idade}' ) 
print(f'A altura média dos alunos maiores de 20 anos é : {media_altura/contador_altura}')

     