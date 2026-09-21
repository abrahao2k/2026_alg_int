'''2 - Crie uma lista vazia e permita que o usuário insira
números inteiros. Use um loop while para 
inserir cada número na lista no índice 0
(usando insert(0, numero)). No final mostre a lista.'''

numeros=[]

cont = 1            # val inicial
while cont <= 5 :   # teste lógico
    
    num = int(input("Digite o valor: "))
    numeros.insert(0,num)
    
    cont = cont + 1 # incremento

print(numeros)