import csv
import os

existe = os.path.exists("produtos.csv")  # verifica se existe

arq = open("produtos.csv","a",newline="")
grav = csv.writer(arq, delimiter=";")

if not existe:
    grav.writerow(["Nome","Preço","Estoque"]) # cabeçalho só se não existe

while True:
    nome  = input("Nome do prod.: ")
    preco = input("Preço: ")
    est   = input("Estoque: ")
    grav.writerow([nome, preco, est])
    print("Gravado.")
    op = input("Outro? (s/n) ")
    if op == 'n' : break

arq.close()