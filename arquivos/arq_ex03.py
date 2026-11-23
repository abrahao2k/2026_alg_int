'''3. Escreva um programa que lê os dados gravados
pelo programa anterior e exibe na tela a 
lista de filmes.'''

try:
    arq = open("filmes.txt","r")
    filmes = arq.read()
    arq.close()
    
    print(filmes)
    
except:
    print("Erro fatal!")





