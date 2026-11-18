import csv

arq = open("produtos.csv","r", newline="")

leitor = csv.DictReader(arq, delimiter=";")

for linha in leitor:
    print(linha["Nome"])
    print(linha["Preço"])
    print(linha["Estoque"] + "\n")


arq.close()