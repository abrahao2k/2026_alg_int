'''3 - Crie uma lista com números repetidos.
peça ao usuário para digitar um número. Use um loop 
while para remover todas as ocorrências desse número da lista.'''

lista = [1, 2, 5, 7, 3, 1, 4, 5, 6, 8, 9, 2, 4, 6, 7, 3, 1]
print(lista)

num = int(input("Remover qual número? "))

while num in lista:
    lista.remove(num)   # remove um elemento

print(lista)

