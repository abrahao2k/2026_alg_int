'''8 - Crie uma lista com números aleatórios.
Peça ao usuário para digitar um número. Use um loop 
while para substituir todas as ocorrências desse
número por zero na lista.'''

import random

lista = []
cont=1
while cont<=20:
    sorteio = random.randint(1,10) # sorteia um número entre 1 e 10
    lista.append(sorteio)
    cont += 1

print(lista)

num = int(input("Digite um número para substituir por zero: "))

while num in lista:
    posicao = lista.index(num)
    lista[posicao] = 0

print(lista)