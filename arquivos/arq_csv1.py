import csv
arq = open("produtos.csv","w",newline="")

grav = csv.writer(arq)
grav.writerow(["Nome","Preço","Estoque"])

while True:
    nome  = input("Nome do prod.: ")
    preco = input("Preço: ")
    est   = input("Estoque: ")
    grav.writerow([nome, preco, est])
    print("Gravado.")
    op = input("Outro? (s/n) ")
    if op == 'n' : break

arq.close()