'''Exercício 2: Média de Notas 
Crie um programa que permita ao usuário inserir suas
notas (em valores reais) em uma lista usando um loop
"while". Quando o usuário inserir um valor negativo, o 
programa deve parar de solicitar notas. Em seguida,
calcule a média das notas e exiba-a na tela.'''

notas = list()
while True:                     ## DIGITAÇÃO DAS NOTAS ##
    n = float(input("Nota: "))
    if n >= 0 : notas.append(n)
    else: break
    
print("Média=", sum(notas)/len(notas) )

'''
soma = 0  # armazena a soma das notas
pos  = 0  # posição inicial
while pos < len(notas) :   # percorre até o fim da lista
    soma = soma + notas[pos]
    pos+=1 # vai pra proxima posição

print("Média = ", soma/len(notas) )
'''



