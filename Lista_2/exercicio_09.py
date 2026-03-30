nome = input('Digite o nome :')
portugues = float(input("Digite sua nota em português :"))
matematica = float(input("Digite a sua nota em matemática : "))
gerais = float(input("Digite a sua nota em conhecimentos gerais : "))

media = (portugues+matematica+gerais)/3

situacao = ''
if(media > 5):
    situacao = 'Aprovado'
else:
    situacao = "Reprovado"

print(f"{nome} você foi {situacao}")