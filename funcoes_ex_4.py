'''4.Crie uma função que recebe um número
entre 1 e 7 e imprime o dia da semana.
Considere: 1/domingo, 2/segunda, 
3/terça... 7/sábado. Se o valor não
estiver no intervalo, informar que é inválido.'''

def nomeDoDia(dia):
    if   dia == 1 : return "Domingo"
    elif dia == 2 : return "Segunda-feira"
    elif dia == 3 : return "Terça-feira"
    elif dia == 4 : return "Quarta-feira"
    elif dia == 5 : return "Quinta-feira"
    elif dia == 6 : return "Sexta-feira"
    elif dia == 7 : return "Sábado"
    else          : return "Inválido"

print( "Hoje é", nomeDoDia(1) )