'''2. Escreva um programa que solicite a digitação
de 5 títulos de filme e grave as informações 
em um arquivo chamado filmes.txt. Use o tratamento
de erros.'''

try:
    arq = open("filmes.txt", "a")
    for x in range(5):
        filme = input("Título do filme: ")
        arq.write(filme + "\n")
        print("Gravação ok.")
    arq.close()
except:
    print("Erro acessando o arquivo.")






        