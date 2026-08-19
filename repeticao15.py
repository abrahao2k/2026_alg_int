# exemplo de laço encadeado

# solicite a digitação do número de linhas de uma tabela
# solicite a digitação do número de colunas de uma tabela

# usando laços encadeados, imprima a tabela na tela
# preenchendo todos os espaços com a letra X

linhas = int(input("Quantas linhas? "))
colunas = int(input("Quantas colunas? "))

cont_linha = 1
while cont_linha <= linhas:
    
    cont_coluna = 1
    while cont_coluna <= colunas:
        print("X", end=" ")
        cont_coluna += 1
    
    print(" ") # pular a linha
    cont_linha += 1

    
    