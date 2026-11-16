# LER OS DADOS DE UM ARQUIVO PARA UMA LISTA

arq = open("lista1.txt", "r")
lista = arq.readlines()   # ler cada linha em uma pos da lista
arq.close()

item = lista[0].strip('\n')  # strip remove o '\n' da palavra
print(f"Digitei {item} no teclado.")




