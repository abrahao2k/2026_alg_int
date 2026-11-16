#GRAVAR UMA LISTA EM UM ARQUIVO

lista = []  # lista vazia

for x in range(10):
    palavra = input("Digite uma palavra: ") + "\n"
    lista.append(palavra)

lista.sort() # ordenação

arq = open("lista1.txt", "w")
arq.writelines(lista)          # grava cada pos da lista
arq.close()

print("Arquivo gravado.")