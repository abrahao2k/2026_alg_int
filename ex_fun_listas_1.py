'''1 - Crie uma lista de nomes.
Use um loop while para pedir a digitação de um nome
para pesquisar na lista. Se existir o nome na lista,
exiba "Nome encontrado!" e encerre a repetição.
Caso não encontre, mostre "não encontrado" e peça
outro nome para pesquisar. '''

nomes=['julia','camila','roberto','moises','katia','silvia',
       'carlos','joaquim','priscila','rosangela','maicon',
       'kleber','antonela','maira','maria','flavio','pedro']

while True:
    pesq = input("Nome para pesquisar: ")
    
    if pesq in nomes:
        print("O nome digitado está na lista.")
        break
    else:
        print("NÃO ENCONTRADO.")