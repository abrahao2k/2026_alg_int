'''faça um programa que usa um laço para inserir valores
digitados pelo usuário em uma lista, porém sempre insere
no início da lista.'''

itens = list() # lista vazia

while True:
    coisa = input("Digite: ")
    itens.insert(0, coisa)
    print(itens)
    resp = input("Cadastrar outro? (s/n) ")
    if resp == 'n' : break
