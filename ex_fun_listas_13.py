'''13 - Crie uma lista de números. Encontre e mostre o
valor mínimo e máximo na lista usando as 
funções min() e max().'''

import random

lista = []
cont=1
while cont<=20:
    sorteio = random.randint(1,100) # sorteia um número entre 1 e 100
    lista.append(sorteio)
    cont += 1

print(lista)

print("Menor valor:", min(lista) )
print("Maior valor:", max(lista) )