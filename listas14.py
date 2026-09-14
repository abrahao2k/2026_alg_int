numeros = [17, 6, 42, 91, 8, 22, 14]

print( sorted(numeros) ) # ordena SEM MUDAR as posições na lista

print("original:", numeros)

# INVERTER A LISTA (TRÁS-PARA-FRENTE)

numeros.reverse()
print(numeros)

# ORDENAÇÃO DECRESCENTE (DO MAIOR PRO MENOR)
numeros.sort() # ordem crescente
numeros.reverse() # inverte a lista para ficar decrescente
print(numeros)

numeros.sort(reverse=True) # ordem decrescente em 1 comando
print(numeros)


