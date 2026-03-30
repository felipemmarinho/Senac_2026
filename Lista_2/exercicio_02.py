dia = input('Digite que dia da semana é hoje : ')
palavra = ''
match dia:
    case 'segunda':
        palavra = 'trabalho'
    case 'terça':
        palavra = 'trabalho'
    case 'quarta':
        palavra = 'trabalho'
    case 'quinta':
        palavra = 'trabalho'
    case 'sexta':
        palavra = 'trabalho'
    case 'sábado':
        palavra = 'casa'
    case 'domingo':
        palavra = 'casa'
    case _:
        palavra = 'nenhum'




print(palavra)