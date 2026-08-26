'''Exercício 3: Nomes em uma Lista 
Peça ao usuário para inserir nomes em uma lista
usando um loop "while". Continue pedindo nomes até
que o usuário insira a palavra "fim". Em seguida, exiba
a lista de nomes. '''

pessoas = [] # lista vazia

while True:
    nome = input("Digite o nome: ")
    
    if nome == "fim" :
        break
    else:
        pessoas.append(nome)

print(pessoas)




