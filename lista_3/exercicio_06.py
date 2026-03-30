aluno_Menos_10 = 0
aluno_10_a_15 = 0
aluno_mais_15 = 0
total_aluno = 0


pesquisa = int(input('Digite o número de alunos na pesquisa'))

for i in range(pesquisa):
    vezes_restaurante = int(input('quantas vezes você frequanta o restaurante no último mês : '))
    if vezes_restaurante < 10 :
        aluno_Menos_10 += 1
    elif vezes_restaurante >= 10 and vezes_restaurante < 15:
        aluno_10_a_15 += 1
    else:
        aluno_mais_15 += 1
    total_aluno += 1

print(f'A procentagem de alunos que frequentaram o refeitório nesse último mês menos de 10 vezes foi : {(aluno_Menos_10/(total_aluno))*100:.2f}')    
print(f'A procentagem de alunos que frequentaram o refeitório nesse último mês de 10  a 14 vezes foi : {(aluno_10_a_15/(total_aluno))*100:.2f}')    
print(f'A procentagem de alunos que frequentaram o refeitório nesse último mês acima de 15 vezes foi : {(aluno_mais_15/(total_aluno))*100:.2f}')    





