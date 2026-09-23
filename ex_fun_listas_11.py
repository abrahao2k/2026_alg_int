'''11 - Crie uma lista que contenha listas aninhadas (sub-listas).
Use um loop while para percorrer a lista principal e,
dentro desse loop, percorra cada sub-lista para encontrar um valor
específico digitado pelo usuário.'''

principal = [ ["bolo",8.00], ["refri",5.00],
              ["coxinha",6.50], ["sorvete",4.75] ]

produto = input("Qual produto? ")

posicao = 0
while posicao < len(principal) :
    
    if produto == principal[posicao][0]:
        print(principal[posicao])
    
    posicao+= 1
    
print("Fim da pesquisa.")