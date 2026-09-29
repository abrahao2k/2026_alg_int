# sequencia decrescente
# range(100,9, -10) # incremento negativo

print(list(range(100,9,-10))) # de 100 até 10

print(list(range(35,-1, -5)))  # de 35 até 0

## MESMA SEQUENCIA USANDO WHILE ##
numeros=[]
cont = 35
while cont >= 0 :
    numeros.append(cont)
    cont -= 5
print(numeros)
