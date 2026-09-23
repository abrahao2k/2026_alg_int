'''9 - Crie uma lista com vários números que se repetem.
Peça ao usuário para digitar um número e conter quantas
vezes esse número aparece na lista. '''

import random

lista = []
cont=1
while cont<=20:
    sorteio = random.randint(1,10) # sorteia um número entre 1 e 10
    lista.append(sorteio)
    cont += 1

print(lista)

num = int(input("Digite um número para contar as ocorrências: "))

print(f"O número {num} aparece {lista.count(num)} vez(es) na lista.")