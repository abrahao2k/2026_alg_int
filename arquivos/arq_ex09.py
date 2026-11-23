''' faça um programa que solicita a digitação
do nome e preço de produtos e grava em arquivo
formato CSV. use um laço para repetir
se o usuário desejar'''
import csv
arq = open("prod.csv", "w", newline="")
grav = csv.writer(arq, delimiter=";")
grav.writerow(["Produto","Preço"])
while True:
    nome = input("Produto: ")
    preço = input("Preço: ")
    grav.writerow([nome,preço])
    resp = input("Gravação Ok. Digitar outro? (s/n) ")
    if resp == 'n' : break
arq.close()


