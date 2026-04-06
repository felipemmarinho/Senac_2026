existe_aluno = -1
ate_9 = 0
mais_10_menos_15 = 0
acima_15 = 0
total_aluno = 0

while existe_aluno != 0:
    existe_aluno = int(input('Quantas vezes você utilizou o restaurante esse último mês :'))
    if (int(existe_aluno) < 10):
        ate_9 += 1
    elif (existe_aluno >= 10) and (existe_aluno < 15):
        mais_10_menos_15 += 1
    else:
        acima_15 += 1

    total_aluno += 1
    
porc_ate_9 = (ate_9/total_aluno) * 100
proc_10_a_15 = (mais_10_menos_15/total_aluno) *100
porc_acima_15 = (acima_15/total_aluno) * 100 

print(f'A procentagem de alunos que frequentaram o refeitório nesse último mês menos de 10 vezes foi : {porc_ate_9:.2f}')    
print(f'A procentagem de alunos que frequentaram o refeitório nesse último mês de 10  a 14 vezes foi : {proc_10_a_15:.2f}')    
print(f'A procentagem de alunos que frequentaram o refeitório nesse último mês acima de 15 vezes foi : {porc_acima_15:.2f}')



