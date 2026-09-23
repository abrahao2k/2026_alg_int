'''4 - Use uma repetição while para preencher uma
lista com numeros variados em qualquer ordem.
Depois ordene os valores em ordem crescente usando
o método sort(). Mostre a lista ordenada.'''
numeros = []

cont=1
while cont <=10:
    num = int(input("Digite: "))
    numeros.append(num)
    cont += 1

numeros.sort() # ordena a lista
print(numeros)