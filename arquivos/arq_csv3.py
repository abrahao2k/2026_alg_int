import csv

arq = open("produtos.csv","r", newline="")

leitor = csv.reader(arq, delimiter=";")
# DictReader - para trabalhar com dicionários ao invés de listas

dados=[]

for linha in leitor:
    dados.append(linha)

print(dados) # lista com sublistas
print(dados[1][0]) # um item de uma sublista

arq.close()