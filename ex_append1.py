'''Exercício 1: Preenchimento de Lista 
Escreva um programa que peça ao usuário para inserir
números inteiros positivos e os armazene em uma lista.
O programa deve continuar pedindo números até que o 
usuário insira um número negativo. Em seguida, exiba a
lista resultante. '''

numeros = []  # list()

while True:   # laço infinito
    
    num = int(input("Digite um número positivo: "))
    
    if num >= 0 :
        numeros.append(num) # acrescenta na lista
    else:
        break # finaliza a repetição

print(numeros)




